import streamlit as st

st.title("🥩 แอปพลิเคชั่นคำนวณราคาหมูรวม VAT 7%")

# ราคาหมู
prices = {
    "หมูสันคอ": 180,
    "หมูสามชั้น": 200,
    "หมูสันใน": 190,
    "หมูบด": 160,
    "ซี่โครงหมู": 180
}

# เลือกชนิดหมู
pork_type = st.selectbox("เลือกชนิดหมู:", list(prices.keys()))

# กรอกจำนวน
weight = st.number_input("กรอกจำนวน (กิโลกรัม):", min_value=0.0, value=1.0)

# คำนวณ
price = prices[pork_type] * weight
vat = price * 0.07
net_price = price + vat

st.header(f"🥩 {pork_type}")
st.write(f"ราคาต่อกิโลกรัม: {prices[pork_type]:.2f} บาท")
st.write(f"น้ำหนัก: {weight:.2f} กิโลกรัม")
st.write(f"VAT 7%: {vat:.2f} บาท")
st.header(f"💰 ราคาสุทธิ: {net_price:.2f} บาท")

st.divider()
st.write("นางสาวธนภรณ์ สุวรรณไพโรจน์ เลขที่ 26 ม.4/4")
