import React from "react";
import { PropTypes } from "prop-types";



const Characters = (props) => {
  return (
  <>
     
    <div class="card-group">
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/characters/1.jpg" />
    <div class="card-body">
      <h5 class="card-title">Luke Skywalker</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/characters/5.jpg" />
    <div class="card-body">
      <h5 class="card-title">Leia Organa</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/characters/3.jpg" />
    <div class="card-body">
      <h5 class="card-title">R2-D2</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/characters/11.jpg" />
    <div class="card-body">
      <h5 class="card-title">Anakin Skywalker</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  
</div>

      
    </>
  
  );
};


export default Characters;

