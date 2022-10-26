'use strict';

class LikeButton extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }

  render() {
    if (this.state.liked) {
      return (
        <button
          className="unliked"
          onClick={() => this.setState({ liked: false })}
        >
          Unliked
        </button>
      );
    }
    return (
      <button className="like" onClick={() => this.setState({ liked: true })}>
        Like
      </button>
    );
  }
}
const base = document.getElementById('root');
ReactDOM.render(<LikeButton />, base);
