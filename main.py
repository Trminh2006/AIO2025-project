import streamlit as st

USERS = ['admin']

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def factorial_calculator():
    st.title("Tính Giai Thừa")
    st.write(f"Chào mừng bạn, {st.session_state.user_name}!")
    number = st.number_input("Nhập một số nguyên không âm:", min_value=0)
    if st.button("Tính giai thừa"):
        result = factorial(number)
        st.success(f"Giai thừa của {number} là: {result}")

    if st.button("Đăng xuất"):
        st.session_state.logged_in = False
        st.session_state.user_name = ""
        st.success("Đăng xuất thành công!")
        st.rerun()

def login():
    st.title("Trang Đăng nhập")
    username = st.text_input("Tên đăng nhập")
    password = st.text_input("Mật khẩu", type="password")
    if st.button("Đăng nhập"):
        if username:
            if username in USERS:
                st.session_state.user_name = username
                st.session_state.logged_in = True
                st.success(f"Đăng nhập thành công, {username}!")
                st.rerun()
                factorial_calculator()
            else:
                st.error("Tên đăng nhập không hợp lệ.")
                st.session_state.logged_in = False
                st.session_state.user_name = username
        else:
            st.warning("Vui lòng nhập tên đăng nhập.")

def main():
    st.title("Ứng dụng tính giai thừa")
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "user_name" not in st.session_state:
        st.session_state.user_name = ""

    if st.session_state.logged_in:
        factorial_calculator()
    else:
        login()

if __name__ == "__main__":
    main()