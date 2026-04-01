import streamlit as st
import pandas as pd

st.title("💼 Transaction Matching System")

file1 = st.file_uploader("Upload Bank CSV")
file2 = st.file_uploader("Upload Company CSV")

if file1 and file2:
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    # Merge
    merged = pd.merge(
        df1, df2,
        on="TransactionID",
        how="outer",
        suffixes=('_bank', '_company'),
        indicator=True
    )

    # Matched
    matched = merged[
        (merged['_merge'] == 'both') &
        (merged['Amount_bank'] == merged['Amount_company']) &
        (merged['Date_bank'] == merged['Date_company'])
    ]

    # Mismatched
    mismatched = merged[
        (merged['_merge'] == 'both') &
        (
            (merged['Amount_bank'] != merged['Amount_company']) |
            (merged['Date_bank'] != merged['Date_company'])
        )
    ]

    # Missing
    missing = merged[merged['_merge'] != 'both']

    # ---- DISPLAY ----
    st.subheader("📊 Summary")
    st.write(f"✅ Matched: {len(matched)}")
    st.write(f"⚠️ Mismatched: {len(mismatched)}")
    st.write(f"❌ Missing: {len(missing)}")

    # Tabs for clean UI
    tab1, tab2, tab3, tab4 = st.tabs(["Merged", "Matched", "Mismatched", "Missing"])

    with tab1:
        st.dataframe(merged)

    with tab2:
        st.dataframe(matched)

    with tab3:
        st.dataframe(mismatched)

    with tab4:
        st.dataframe(missing)