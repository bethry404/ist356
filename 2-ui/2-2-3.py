import streamlit as st

st.title('Order File Processing')

selected_file = st.file_uploader("Select a file", type=['txt'])

total = 0.0
count = 0
if selected_file is not None:
    contents = selected_file.read().decode('utf-8')
    for line in contents.splitlines():
        num = float(line.strip()) if line.strip() else 0.0
        total += num
        count +=1





st.markdown(f''' 
### File Processing Results
- Total: ${total}
- Count: {count}
''')