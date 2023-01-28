import { useState } from 'react';

export function Text() {
	const [title, setTitle] = useState<string>('Padrão');
	return (
    <>
	    <input type="text" placeholder="Digite o nome..." onChange={e => setTitle(e.target.value)}/>
	    <h1>{title}</h1>
    </>
	)
}