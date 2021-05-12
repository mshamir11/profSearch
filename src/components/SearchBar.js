import React from "react";
import "./SearchBar.css";
class SearchBar extends React.Component {
  // onInputChange(event) {
  //   console.log(event.target.value);
  // }

  state = { term: " " };
  query_option = { option: "research_interest" };
  onSubmit(event) {
    event.preventDefault();

    this.props.onSearchSub(this.state.term, this.query_option.option);
    console.log("this is inside search bar", this.state.term);
  }

  render() {
    return (
      <div className="ui segment">
        <form onSubmit={(e) => this.onSubmit(e)} className="ui form">
          <label htmlFor="" className="segment placeholder">
            <h1 style={{ fontSize: "50px" }}>
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
          </label>

          <div className="field">
            <div className="">
              <div class="ui small  input">
                <select
                  onChange={(e) => {
                    this.query_option.option = e.target.value;
                    // console.log(e.target.value);
                  }}
                  className="ui dropdown select-input"
                >
                  <option value="research_interest" selected>
                    {" "}
                    Research Interest{" "}
                  </option>
                  <option value="professor_name"> Professor Name </option>
                  <option value="university_name"> University Name </option>
                </select>
                <div className="ui input input-width">
                  <input
                    type="text"
                    value={this.state.term}
                    className="prompt"
                    onChange={(e) => {
                      this.setState({ term: e.target.value });
                    }}
                  />
                </div>
              </div>
            </div>
          </div>
        </form>
        {/* <div className="float-container">
          <div className="field">
            <div className="ui search">
              <div className="ui icon input">
                <input
                  type="text"
                  value={this.state.term}
                  className="prompt"
                  onChange={(e) => {
                    this.setState({ term: e.target.value });
                  }}
                />
              </div>
            </div>
          </div>
        </div> */}
      </div>
    );
  }
}

export default SearchBar;
