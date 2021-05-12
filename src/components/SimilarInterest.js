import React from "react";

const SimilarInterest = () => {
  const similar = ["Machine Learning", "Deep Learning"];
  return (
    <div className="">
      <h2 style={{ color: "black" }}>Similar Research Interests:</h2>

      {similar.map((topic) => {
        return (
          <span style={{ fontSize: "16px" }}>
            <a href="#">{"\xa0\xa0" + topic + "\xa0\xa0\xa0"} </a>
          </span>
        );
      })}
    </div>
  );
};

export default SimilarInterest;
