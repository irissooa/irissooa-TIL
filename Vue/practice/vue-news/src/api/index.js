import axios from 'axios';

const config = {
  baseURL : "	https://api.hnpwa.com/v0/",
};

function fetchNews() {
  return axios.get(`${config.baseURL}news/1.json`);
}

function fetchAsk() {
  return axios.get(`${config.baseURL}ask/1.json`);
}

function fetchJobs(){
  return axios.get(`${config.baseURL}jobs/1.json`);
}

function fetchUser(id){
  const url = `${config.baseURL}user/${id}.json`;
  return axios.get(url);
}

function fetchItem(id){
  const url =`${config.baseURL}item/${id}.json`;
  return axios.get(url);
}

function fetchList(type) {
  const url = `${config.baseURL}${type}/1.json`;
  return axios.get(url);
}

export {
  fetchNews,
  fetchAsk,
  fetchJobs,
  fetchUser,
  fetchItem,
  fetchList
}