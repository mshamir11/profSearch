import React from "react";
import "./HomePage.css";

class HomePage extends React.Component {
  state = { term: " " };
  query_option = { option: "research_interest" };

  onSubmit(event) {
    event.preventDefault();

    this.props.onSearchSub(this.state.term, this.query_option.option);
    // console.log("this is inside Home page", this.state.term);
  }

  render() {
    return (
      <div>
        <div className="centered ">
          <div>
            <div
              style={{
                marginBottom: "50px",
                display: "flex",
                justifyContent: "center",
              }}
              className=""
            >
              <h1 style={{ fontSize: "100px" }}>
                <span style={{ color: "#4285F4" }}>P</span>
                <span style={{ color: "#DB4437" }}>r</span>
                <span style={{ color: "#F4B400" }}>o</span>
                <span style={{ color: "#4285F4" }}>f</span>
                <span style={{ color: "#0F9D58" }}>S</span>
                <span style={{ color: "#DB4437" }}>e</span>
                <span style={{ color: "#F4B400" }}>a</span>
                <span style={{ color: "#0F9D58" }}>r</span>
                <span style={{ color: "#4285F4" }}>c</span>
                <span style={{ color: "#DB4437" }}>h</span>
              </h1>
            </div>
          </div>

          <form
            style={{ textAlign: "center" }}
            onSubmit={(e) => this.onSubmit(e)}
          >
            <span className=" home-input">
              <input
                className=""
                onChange={(e) => {
                  this.setState({ term: e.target.value });
                }}
              />

              <div style={{ marginTop: "10px" }} className="">
                <label style={{ fontSize: "20px" }}>
                  Choose a search type:{" "}
                </label>
                <select
                  id="myList"
                  onChange={(e) => {
                    this.query_option.option = e.target.value;
                  }}
                >
                  <option value="research_interest" selected>
                    {" "}
                    Research Interest{" "}
                  </option>
                  <option value="professor_name"> Professor Name </option>
                  <option value="university_name"> University Name </option>
                </select>
              </div>
            </span>
          </form>
        </div>
      </div>
    );
  }
}

export default HomePage;
