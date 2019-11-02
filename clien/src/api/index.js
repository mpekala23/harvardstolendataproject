const API_URL = "http://127.0.0.1:5000";
import axios from 'axios'

export function authenticate (user_data) {
  return axios.post(API_URL + '/login', user_data);
}

export function submit_article(article_data, jwt) {
  return axios.post(API_URL + '/add-article',
    article_data,
    {
      headers: {
        Authorization: `Bearer: ${jwt}`,
        'Content-Type': 'multipart/form-data'
      }
    });
}

export function get_articles() {
  return axios.get(API_URL + '/get-articles');
}

export function get_article(id) {
  return axios.get(API_URL + '/get-article', { params: {id:id} });
}
