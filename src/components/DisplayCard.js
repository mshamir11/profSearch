import "./DisplayCard.css";
import React from "react";

const DisplayCard = (props) => {
  // console.log(props.details.Name);

  return (
    <div className="Card">
      <div className="upper-container">
        <div className="image-container">
          <img src={props.details.Pic} alt="" height="100px" width="100px" />
        </div>

        <div style={{ translate: "0px -100px", padding: "5px" }} className="">
          <div style={{ padding: "5px" }}>
            <a
              href={props.details.Google_Scholar_url}
              target="_blank"
              className="href"
            >
              <i className="ai ai-google-scholar-square ai-2x"></i>
            </a>
          </div>

          <div style={{ padding: "5px" }} className="div">
            <a
              href={props.details.Homepage_url}
              target="_blank"
              className="href"
            >
              <i className="icon-home icon-2x" dataFaTransform="down-10"></i>
            </a>
          </div>
          <div style={{ padding: "5px" }}>
            <a
              href={props.details.Google_Scholar_url}
              target="_blank"
              className="href"
            >
              <i className="ai ai-obp ai-2x"></i>
            </a>
          </div>
        </div>
      </div>

      <div className="middle-container">
        <h1>{props.details.Name}</h1>
        <h3 style={{ marginTop: "-15px" }}>{props.details.Affiliation}</h3>

        <p>
          <h4>Research Interests</h4>
          {props.details.Research_Interests.map((item) => {
            return item + ",";
          })}
        </p>
      </div>

      <div className="lower-container">
        <table
          style={{ background: "cornflowerblue", fontSize: "16px" }}
          className="btn center"
        >
          <tr>
            <th>H Index | </th>
            <th> Total Citations |</th>
            <th> i-Index</th>
          </tr>
          <tr>
            <td>
              <h2>{props.details.hindex}</h2>
            </td>
            <td>
              <h2>{props.details.Total_Citations}</h2>
            </td>
            <td>
              <h2>{props.details.i10index}</h2>
            </td>
          </tr>
        </table>
      </div>
    </div>
  );
};

export default DisplayCard;
