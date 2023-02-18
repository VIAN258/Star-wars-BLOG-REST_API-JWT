import React from "react";
import { PropTypes } from "prop-types";
import { useEffect, useState } from "react";


const characters = [
  {
    'index' : 1,
    'name' : "Luke Skywalker"
  },
  {
    'index' : 5,
    'name' : "Leia Organa"
  },
  {
    'index' : 3,
    'name' : "R2-D2"
  },
  {
    'index' : 11,
    'name' : "Anakin Skywalker"
  },
]

const Characters = (props) => {
  const [info, setInfo] = useState ({"name": " "}, {"height": " "}, {"gender": " "}, {"mass": " "}, {"hair_color": " "}, {"skin_color": " "}, {"birth_year": " "}) 
  /*useEffect (() =>{
    const getInfocharacter = async () => {
      const  response  = await fetch(`https://www.swapi.tech/api/people/`)
      const characters = response.json
    }
  })*/
   

  const getInfo =  async (index) => {
    const response = await fetch (`https://www.swapi.tech/api/people/${index}`)
    const people = await response.json()
    setInfo (people.result.properties)
  }
  return (
  <>
     
    <div className="card-group">
      { characters.map((c) => (
     
       <div className="card">
       <img src={`https://starwars-visualguide.com/assets/img/characters/${c.index}.jpg`}/>
         <div className="card-body">
           <h5 className="card-title">{c.name}</h5>
           <button type="button" onClick={()=> getInfo(c.index)} className="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleModal">Detalles</button>
           <button type="button" className=  " btn btn-outline-danger border-0">
                 <i className="far fa-heart"></i>
           </button>
         </div>
         </div> 
      ))}
  </div>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h1 class="modal-title fs-5" id="exampleModalLabel">{info.name}</h1>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <p>
          Height:{info.height}
        </p>
        <p>
          Mass: {info.mass}
        </p>
        <p>
          Hair color: {info.hair_color}
        </p>
        <p>
          Skin color: {info.skin_color}
        </p>
        <p>
          Birth year: {info.birth_year}
        </p>
        <p>
         Gender: {info.gender}
        </p>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div>
    </>
  );
};


export default Characters;

