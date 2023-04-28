import { initializeApp} from 'firebase/app'
import { getFirestore, collection, query, where, getDocs, setDoc, doc } from 'firebase/firestore/lite'

// const firebaseConfig = {
//     apiKey: "AIzaSyCBfJ5QsytSQqkipNUqk7cbHl5chQ9A-hk",
//     authDomain: "video-indexing-project.firebaseapp.com",
//     projectId: "video-indexing-project",
//     storageBucket: "video-indexing-project.appspot.com",
//     messagingSenderId: "135604416968",
//     appId: "1:135604416968:web:b03e6d36113324991f10fd"
//   };
  

const app = initializeApp(process.env.FIREBASE_CONFIG);
const db = getFirestore(app)

async function getAllVideos(){
    const videoCollection = collection(self.db, 'videos');
    const videoSnapshot = await getDocs(videoCollection);
    const videoList = videoSnapshot.docs.map(doc => doc.data());
    return JSON.stringify(videoList);
}

async function getSingleVideo(videoName){
    const videoCollection = collection(self.db, 'videos');
    const nameQuery = query(videoCollection, where("name", ">=", videoName));
    const querySnapshot = await getDocs(q);
    const videoList = querySnapshot.docs.map(doc => doc.data());
    return JSON.stringify(videoList);
}

async function pushVideo(videoJsonData){
    await setDoc(doc(db,'videos'),videoJsonData);
}