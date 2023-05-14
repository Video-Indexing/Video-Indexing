import axios from 'axios';

const SearchVideoByName = async (name) => {
    let res;
    await axios.get("http://127.0.0.1:5050/searchVideoByName?name=" + name).then(
        (r) => {
            console.log(r.data);
            res= r;    
        }
    );
    // if()
    return res.data;
};

export {SearchVideoByName};