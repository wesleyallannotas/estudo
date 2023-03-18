// $ - Usado para referenciar estrutura do dom
function convertToHtml(virtualNode) {
  if (typeof virtualNode === 'string' || typeof virtualNode === 'number') {
    return document.createTextNode(`${virtualNode}`);
  }

  const $domElement = document.createElement(virtualNode.tagName);

  virtualNode.props.children.forEach(virtualChild => {
    $domElement.appendChild(convertToHtml(virtualChild));
  });

  return $domElement;
}

// $ - Usado para referenciar estrutura do dom
function render(initialVirtualTree, $domRoot) {
  const $appHtml = convertToHtml(initialVirtualTree);
  console.log($appHtml);
  $domRoot.appendChild($appHtml);
}

function createElement(elementType, props, ...children) {
  const virtualElementsProps = {
    ...props,
    children,
  };

  if (typeof elementType === 'function') {
    return elementType(virtualElementsProps);
  }

  return {
    tagName: elementType,
    props: virtualElementsProps,
  };
}

const React = {
  createElement,
};

function Title() {
  return React.createElement('h1', null, 'Contador');
}

function AppRaw(props) {
  return React.createElement(
    'section',
    {
      className: 'App',
    },
    React.createElement(Title, null),
    React.createElement(
      'div',
      null,
      React.createElement('div', null, '0'),
      React.createElement('button', null, 'Incrementar'),
      React.createElement('button', null, 'Decrementar')
    )
  );
}

// Caso possua Babel, funcionara JSX
// function App() {
//   return (
//     <section className="app">
//       <h1>Contador</h1>
//       <div>
//         <div>0</div>
//         <button>Incrementar</button>
//         <button>Decrementar</button>
//       </div>
//     </section>
//   );
// }

// render(<App />, document.getElementById('#root'));
render(React.createElement(AppRaw, null), document.getElementById('root'));
