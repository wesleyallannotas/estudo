class App extends React.Component {
  constructor(props) {
    super(props);
    this.state = { imc: 0, resultado: '' };
    this.handleChange = this.handleChange.bind(this);
  }

  handleChange(e) {
    let altura = Number(document.getElementById('altura').value);
    let peso = Number(document.getElementById('peso').value);
    this.calculaImc(peso, altura);
  }

  calculaImc(peso, altura) {
    let imcRaw = peso / (altura * altura);
    let formattedImc = imcRaw.toFixed(2).replace('.', ',');
    this.setState({ imc: formattedImc });
    imcResultText();
  }

  imcResultText() {
    if (this.state.imc < 16) {
      this.setState({ resultado: 'Invalido!' });
    } else if (this.state.imc < 17) {
      this.setState({ resultado: 'Muito abaixo do peso' });
    } else if (this.state.imc < 18.5) {
      this.setState({ resultado: 'Abaixo do peso' });
    } else if (this.state.imc < 25) {
      this.setState({ resultado: 'Peso normal' });
    } else if (this.state.imc < 30) {
      this.setState({ resultado: 'Acima do peso' });
    } else if (this.state.imc < 35) {
      this.setState({ resultado: 'Obesidade grau I' });
    } else if (this.state.imc < 40) {
      this.setState({ resultado: 'Obesidade grau II' });
    } else {
      this.setState({ resultado: 'Obesidade grau III' });
    }
  }

  render() {
    return (
      <div className="container">
        <div className="entrada">
          <label>
            Peso (kg):
            <br />
            <input id="peso" type="number" onChange={this.handleChange} />
            <br />
          </label>
          <label>
            Altura (m):
            <br />
            <input id="altura" type="number" onChange={this.handleChange} />
          </label>
        </div>
        <hr />
        <div className="exibi">
          <h1>O seu imc:</h1>
          <h1>{this.state.imc}</h1>
          <h1>{this.state.resultado}</h1>
        </div>
      </div>
    );
  }
}

const root = document.getElementById('root');
ReactDOM.render(<App />, root);
