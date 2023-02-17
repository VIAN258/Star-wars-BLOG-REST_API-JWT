import React from "react";
import "../../styles/home.css";
import Characters from "../component/characters";
import Planets from "../component/planets";
import Aircrafts from "../component/aircrafts";

export const Home = () => (
	<div className="container">
		<h2 className="text-light py-4">Personajes</h2>
			<Characters />
		<h2 className="text-light py-4">Planetas</h2>
		    <Planets />
		<h2 className="text-light py-4">Vehiculos</h2>
		    <Aircrafts />
	</div>
);

