import React from "react";
import { useEffect, useState, useContext } from "react";
import { Context } from "../store/appContext";



const aircrafts = [
  {
    'index' : 10,
    'name' : "Millennium Falcon"
  },
  {
    'index' : 12,
    'name' : "X-wing"
  },
  {
    'index' : 13,
    'name' : "TIE Advanced"
  },
  {
    'index' : 15,
    'name' : "Executor"
  },
]

const Aircrafts = () => {
  const [info, setInfo] = useState ({"name": " "}, {"model": " "}, {"starship_class": " "}, {"manufacturer": " "}, {"crew": " "}, {"cargo_capacity": " "}, {"hyperdrive_rating": " "}) 
  const { store, actions } = useContext(Context);


  const getInfo =  async (index) => {
    const response = await fetch (`https://www.swapi.tech/api/starships/${index}`)
    const starships = await response.json()
    setInfo (starships.result.properties)
  }
  return (
  <>
     
    <div className="card-group">
    { aircrafts.map((c) => (

  <div className="card" key={c.index +100}>
  <img src={`https://starwars-visualguide.com/assets/img/starships/${c.index}.jpg`} />
    <div className="card-body">
      <h5 className="card-title">{c.name}</h5>
      <button type="button" onClick={()=> getInfo(c.index)} className="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#aircraftModal">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0" onClick={()=> actions.addFavorites(c.name)}>
            <i className="far fa-heart"></i>
      </button>
    </div>
    </div>
 ))}
 </div>
 <div class="modal fade" id="aircraftModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
 <div class="modal-dialog">
   <div class="modal-content">
     <div class="modal-header">
       <h1 class="modal-title fs-5" id="exampleModalLabel">{info.name}</h1>
       <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
     </div>
     <div class="modal-body">
       <p>
        Model:{info.model}
       </p>
       <p>
        Starship class: {info.starship_class}
       </p>
       <p>
        Manufacturer: {info.manufacturer}
       </p>
       <p>
        Crew: {info.crew}
       </p>
       <p>
        Cargo_capacity: {info.cargo_capacity}
       </p>
       <p>
        Hyperdrive_rating: {info.hyperdrive_rating}
       </p>
     </div>
     <div class="modal-footer">
       <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
     </div>
   </div>
 </div>
</div>
   </>
 );
};
  

export default Aircrafts;