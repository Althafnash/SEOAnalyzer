import streamlit as st
from Keyword import google_suggestions, get_result_count
from On_Page_SEO import Analyzer
from pytrends.request import TrendReq
import pandas

st.set_page_config(page_title="SEO Analyzer", layout="centered")

st.title("🔍 SEO Analyzer")

# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs(["Keyword Research", "Search Result Count", "On-Page SEO", "Download", "Google Trends"])

# Shared keyword input
with tab1:
    keyword = st.text_input("Enter a keyword:", placeholder="e.g., python programming", key="keyword")

    if keyword:
        st.subheader("Google Suggestions")
        suggestions = google_suggestions(keyword)
        if suggestions:
            for s in suggestions:
                st.write("-", s)
        else:
            st.warning("No suggestions found.")

with tab2:
    if keyword:
        st.subheader("Search Result Count")
        count = get_result_count(keyword)
        st.success(f"{count}")
    else:
        st.info("Please enter a keyword in the 'Keyword Research' tab.")

with tab3:
    url = st.text_input("Enter a URL to analyze:", placeholder="e.g., https://example.com", key="url")

    if url:
        st.subheader("On-Page SEO Report")
        try:
            PageSEO = Analyzer(url)
            for section in PageSEO:
                st.markdown("--------")
                st.write(section)
        except Exception as e:
            st.error(f"Failed to analyze URL: {e}")

with tab4:
    suggestions = google_suggestions(keyword)
    count = get_result_count(keyword)
    df = pandas.DataFrame({"Keyword Suggestions": suggestions})
    df['Search Results Count'] = count
    st.download_button("Download CSV", df.to_csv(index=False), file_name="SEO_keywords.csv")

with tab5:
    suggestions = google_suggestions(keyword)
    pytrend = TrendReq()
    pytrend.build_payload([keyword], timeframe="today 12-m")
    trends = pytrend.interest_over_time()
    st.line_chart(trends[keyword])