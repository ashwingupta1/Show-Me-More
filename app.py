import streamlit as st
import bz2file as bz2
import pickle

st.set_page_config(layout="wide")

def load_compressed_pickle(file_path):
    with bz2.BZ2File(file_path, 'rb') as f:
        return pickle.load(f)

shows = load_compressed_pickle('shows_list.pbz2')
similarity = load_compressed_pickle('similarity.pbz2')
shows_list = shows['name'].values


def fetch_poster(show_id):
    p_url = shows.loc[shows.index == show_id, 'poster_path'].values
    full_url = "https://image.tmdb.org/t/p/w500" + p_url[0]
    return full_url


def recommend(show):
    index = shows[shows['name']==show].index[0]
    distance = sorted(list(enumerate(similarity[index])),reverse = True, key=lambda vector: vector[1])
    applicable_poster = []
    recommended_shows = []
    for i in distance[1:6]:
        show_index = i[0]
        recommended_shows.append(shows.iloc[i[0]]["name"])
        applicable_poster.append(fetch_poster(show_index))
    return recommended_shows, applicable_poster


st.header('Show Me More')

st.write('<div style="margin-bottom: 10px;"></div>', unsafe_allow_html=True)

selected_show = st.selectbox("Select a show you already like", shows_list)

if st.button("Show Recommendations"):
    s_names, s_poster = recommend(selected_show)
    st.write('<div style="margin-bottom: 5px;"></div>', unsafe_allow_html=True)
    st.write("If you like " + selected_show + ", you may also like:")
    col1, col2, col3, col4, col5 = st.columns(5)

    # Define CSS for center alignment and font size
    center_css = 'style="text-align: center; font-size: 16px;"'  # Adjust font size as needed

    with col1:
        st.image(s_poster[0])
        homepage_url = shows.loc[shows["name"] == s_names[0], "homepage"].values
        if str(homepage_url[0]) != 'nan' and homepage_url[0] != "":
            st.write(f'<div {center_css}><a href="{homepage_url[0]}" target="_blank">{s_names[0]}</a></div>', unsafe_allow_html=True)
        else:
            st.write(f'<div {center_css}>{s_names[0]}</div>', unsafe_allow_html=True)

    with col2:
        st.image(s_poster[1])
        homepage_url = shows.loc[shows["name"] == s_names[1], "homepage"].values
        if str(homepage_url[0]) != 'nan' and homepage_url[0] != "":
            st.write(f'<div {center_css}><a href="{homepage_url[0]}" target="_blank">{s_names[1]}</a></div>', unsafe_allow_html=True)
        else:
            st.write(f'<div {center_css}>{s_names[1]}</div>', unsafe_allow_html=True)


    with col3:
        st.image(s_poster[2])
        homepage_url = shows.loc[shows["name"] == s_names[2], "homepage"].values
        if str(homepage_url[0]) != 'nan' and homepage_url[0] != "":
            st.write(f'<div {center_css}><a href="{homepage_url[0]}" target="_blank">{s_names[2]}</a></div>', unsafe_allow_html=True)
        else:
            st.write(f'<div {center_css}>{s_names[2]}</div>', unsafe_allow_html=True)

    with col4:
        st.image(s_poster[3])
        homepage_url = shows.loc[shows["name"] == s_names[3], "homepage"].values
        if str(homepage_url[0]) != 'nan' and homepage_url[0] != "":
            st.write(f'<div {center_css}><a href="{homepage_url[0]}" target="_blank">{s_names[3]}</a></div>', unsafe_allow_html=True)
        else:
            st.write(f'<div {center_css}>{s_names[3]}</div>', unsafe_allow_html=True)
   
    with col5:
        st.image(s_poster[4])
        homepage_url = shows.loc[shows["name"] == s_names[4], "homepage"].values
        if str(homepage_url[0]) != 'nan' and homepage_url[0] != "":
            st.write(f'<div {center_css}><a href="{homepage_url[0]}" target="_blank">{s_names[4]}</a></div>', unsafe_allow_html=True)
        else:
            st.write(f'<div {center_css}>{s_names[4]}</div>', unsafe_allow_html=True)