'use strict';

const e = React.createElement;

class ButtonLike extends React.Component {
  constructor(props) {
    super(props);
    this.state = { liked: false };
  }
  render() {
    if (this.state.liked) {
      return e(
        'button',
        {
          onClick: () => this.setState({ liked: false }),
          className: 'unliked',
        },
        `Unliked`
      );
    }
    return e(
      'button',
      { onClick: () => this.setState({ liked: true }), className: 'like' },
      'Like'
    );
  }
}
const elementoReact = document.getElementById('root');
ReactDOM.render(e(ButtonLike), elementoReact);
