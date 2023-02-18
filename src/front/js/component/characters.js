import React from "react";
import { PropTypes } from "prop-types";




const Characters = (props) => {
  const getInfo =  async (index) => {
    //const response = await fetch (`https://www.swapi.tech/api/people/${index}`)
    console.log("hola")
    //const people = await response.json()
    //console.log(people)
  }
  return (
  <>
     
    <div className="card-group">
  <div className="card">
  <img src="https://starwars-visualguide.com/assets/img/characters/1.jpg" />
    <div className="card-body">
      <h5 className="card-title">Luke Skywalker</h5>
      <button type="button" onClick={()=> getInfo(1)} className="btn btn-secondary">Detalles</button>
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

