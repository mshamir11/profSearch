import React from "react";
import "./DisplayCard.css";
import SearchBar from "./SearchBar";
import DisplayCard from "./DisplayCard";
import SimilarInterest from "./SimilarInterest";
import HomePage from "./HomePage";
import axios from "axios";

class App extends React.Component {
  state = { prof_list: [], status: 0, present_state: 1 };

  onSearchSubmit = async (term, query_option) => {
    // console.log("im here");
    const response = await axios.post("http://localhost:5000/", {
      message: term,
      query_type: query_option,
    });

    // const response = await fetch
    // console.log("this is on search submit", term);
    const data = await response.data;
    // console.log(data);
    // console.log(typeof data);
    this.setState({
      prof_list: data,
      status: 1,
      present_state: !this.state.present_state,
    });
  };

  renderBody() {
    if (this.state.status === 0) {
      return (
        <div className="">
          <HomePage onSearchSub={this.onSearchSubmit} />
        </div>
      );
    }

    if (this.state.status === 1) {
      if (this.state.prof_list.length < 1) {
        return (
          <div style={{ marginTop: "30px" }} className="ui container">
            <div>
              <SearchBar onSearchSub={this.onSearchSubmit} />
            </div>

            <div style={{ marginTop: "10px", fontSize: "15px" }} className="">
              No results found, Please use some other keywords.
            </div>
          </div>
        );
      } else {
        // const display_card = this.state.prof_list.map((prof_data) => {
        //   return <DisplayCard details={prof_data} />;
        // });
        return (
          <div style={{ marginTop: "30px" }} className="ui container">
            <div>
              <SearchBar onSearchSub={this.onSearchSubmit} />
            </div>

            <div style={{ marginTop: "10px" }} className="">
              <SimilarInterest />
            </div>

            <div
              style={{
                marginTop: "30px",
                display: "flex",
                justifyContent: "center",
              }}
              className="ui cards"
            >
              {this.state.prof_list.map((prof_data) => {
                return <DisplayCard details={prof_data} />;
              })}
            </div>
          </div>
        );
      }
    }
  }

  render() {
    // const profs = this.state.prof_list.map((prof) => {
    //   return <DisplayCard details={prof} />;
    // });
    return <div className="">{this.renderBody()}</div>;
  }
}

export default App;
