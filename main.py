import io
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

def calc_avg(scores):
    return sum(scores) / len(scores) if scores else 0

def calc_percent_distribution(scores):
    bins = {'80-100': 0, '60-79': 0, '40-59': 0, '<40': 0}
    for score in scores:
        if 80 <= score <= 100:
            bins['80-100'] += 1
        elif 60 <= score < 80:
            bins['60-79'] += 1
        elif 40 <= score < 60:
            bins['40-59'] += 1
        else:
            bins['<40'] += 1
    return bins

def main():
    st.title("Phân tích điểm số học sinh")
    uploaded_file = st.file_uploader("Chọn file MS Excel", type=["xlsx"])
    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        # get "Diem so" column
        scores = df["Điểm số"].astype(float).tolist()

        # Average score
        avg_score = calc_avg(scores)
        st.write(f"Điểm trung bình: {avg_score:.2f}")

        # Percent distribution
        dist = calc_percent_distribution(scores)
        st.write("Phân phối phần trăm:")
        st.write(dist)

        # Visualize the distribution
        labels = list(dist.keys())
        values = list(dist.values())
        fig, ax = plt.subplots(1, 1, figsize=(10, 5))
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140)
        plt.tight_layout()
        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        img = Image.open(buf)
        st.image(img, caption="Phân phối phần trăm điểm số")

if __name__ == "__main__":
    main()