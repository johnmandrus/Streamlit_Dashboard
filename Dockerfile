CMD mkdir /Streamlit_Dashboard
COPY . /Streamlit_Dashboard

WORKDIR /Streamlit_Dashboard

EXPOSE 8501

RUN pip3 install -r requirements.txt

CMD streamlit run dashboard.py