import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar bg-black px-5 py-4">
			<div className="ml-auto">
			    <img className="navbar-brand container-fluid"src="https://upload.wikimedia.org/wikipedia/commons/2/21/Star_Wars_logo.png" alt="" width="30" height="60"></img>
			</div>
			<div className="ml-auto">
				<div class="btn-group">
					<button type="button" class="btn btn-secondary dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
						Favoritos
					</button>
					<ul class="dropdown-menu dropdown-menu-dark">	
					</ul>
		        </div>
			</div>
		</nav>
	);
};




