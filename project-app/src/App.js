import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import PhotoUploadApp from "./js/PhotoUploadApp";
import UploadResult from "./js/UploadResult";
import Header from "./js/Header";
import Footer from "./js/Footer";
import CustomCircularGauge from "./js/CustomCircularGauge";
function App() {
  return (
    <div className="App">
      <Header />
      <Router>
        <Routes>
          <Route path="/" element={<PhotoUploadApp />} />
          <Route path="/result" element={<UploadResult />} />
        </Routes>
      </Router>
      <Footer />
    </div>
  );
}

export default App;
