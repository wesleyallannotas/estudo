class Clock extends React.Component {
  constructor(props) {
    super(props);
    this.state = { time: new Date() };
  }

  tick() {
    this.setState({ time: new Date() });
  }

  componentDidMount() {
    this.timeID = setInterval(() => this.tick(), 1000);
  }

  componentWillUnmount() {
    clearInterval(this.timeID);
  }

  render() {
    return (
      <div>
        <h1>HORARIO LOCAL</h1>
        <h1> {this.state.time.toLocaleTimeString()} </h1>
      </div>
    );
  }
}

const base = document.getElementById('root');
ReactDOM.render(<Clock />, base);
