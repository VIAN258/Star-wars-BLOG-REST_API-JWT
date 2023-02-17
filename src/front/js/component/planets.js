import React from "react";



const Planets = () => {
  return (
  <>
     
    <div class="card-group">
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/planets/2.jpg" />
    <div class="card-body">
      <h5 class="card-title">Alderaan</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/planets/10.jpg" />
    <div class="card-body">
      <h5 class="card-title">Kamino</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/planets/5.jpg" />
    <div class="card-body">
      <h5 class="card-title">Dagobah</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/planets/4.jpg" />
    <div class="card-body">
      <h5 class="card-title">Hoth</h5>
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

export default Planets;