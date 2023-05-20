var admin = require("firebase-admin");
const { getFirestore,CollectionReference,DocumentReference } = require('firebase-admin/firestore');
require('dotenv').config();

const serviceAccount = require("./serviceAccount.json");

const fireBaseApp = admin.initializeApp({
    credential: admin.credential.cert(serviceAccount),
    databaseURL: process.env.DATABASE_URL
});
const db = getFirestore(fireBaseApp);
const videoCollection = db.collection('videos');
const bookCollection = db.collection('neuralnetworksanddeeplearning')


async function getCollectionData(collection) {
    const docsRef = collection;
    const mainDocs = [];

    const docs = await docsRef.get();
    docs.forEach(async (doc) => {
      mainDocs.push({ ...doc.data(), _id: doc.id });
    });

    return mainDocs;
}

async function searchVideosByTags(videoCollection,queryText, callback){
  videoCollection.where('tags', 'array-contains', queryText)
    .get().then((querySnapshot) => {
      const searchResults = querySnapshot.docs.map((doc) => doc.data());
      callback(null, searchResults); // Pass the search results to the callback function
    })
    .catch((error) => {
      console.log('Error getting documents: ', error);
      callback(error, null); // Pass the error to the callback function
    });
}


async function searchVideo(videoCollection,queryText){
  var newRef = videoCollection.where('name', '>=', queryText).where('name', '<=', queryText+ '\uf8ff');
  // var newSmallerRef = videoCollection.where("name", "<=", videoName);

  const mainDocs = [];

  var docs = await newRef.get();

  docs.forEach(async (doc) => {
    mainDocs.push({ ...doc.data(), _id: doc.id });
  });

    // docs = await newSmallerRef.get();
    // docs.forEach(async (doc) => {
    //     mainDocs.push({ ...doc.data(), _id: doc.id });
    //   });
  

    return mainDocs;
}


async function createVideo(videoCollection,videoObj){
  return await videoCollection.doc()
    .set(videoObj);
}
// module.exports = book;
// module.exports = db;
module.exports.videoCollection = videoCollection;
module.exports.bookCollection = bookCollection;
module.exports.getCollectionData = getCollectionData;
module.exports.createVideo = createVideo;
module.exports.searchVideo = searchVideo;
module.exports.searchVideosByTags = searchVideosByTags;