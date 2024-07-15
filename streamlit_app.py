from mysql_helper import run_mysql_queries
import streamlit as st
from streamlit import connections
conn = st.connection('mysql', type='sql')
# df = conn.query('select * from vectordb.demo_embeddings', ttl=600)

st.title("🎈 MySQL GEN ai Test")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
question = st.text_area("Enter you question:")
if st.button("Ask"):
    query=f"set @query='{question}'; SET @options = JSON_Object('vector_store', JSON_ARRAY('vectordb.demo_embedding')); call sys.ML_RAG(@query,@output,@options); SELECT JSON_UNQUOTE(JSON_EXTRACT(@output, '$.text'));"

    # answer=conn.query("select * from vectordb")
    answer=run_mysql_queries(query)
    if answer is not None:
        st.write(answer[0])
    else:
        st.write("DB connection error")
