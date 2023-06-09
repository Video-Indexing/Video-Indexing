import axios from 'axios';

const UploadVideo = async (name, link) => {
  let res;
  let obj = { name, link };
  // let jsonData = JSON.stringify(obj);
  // console.log(jsonData);
  await axios.post('http://127.0.0.1:5050/uploadVideo', obj).then((r) => {
    // console.log(r.data);
    res = r;
  });
  // if()
  return res;
};

const getVideoSubjects = async () => {
  let res;
  await axios.get('http://127.0.0.1:5050/getAllTopics').then((r) => {
    // console.log(r.data);
    res = r;
  });
};

export { UploadVideo, getVideoSubjects };
