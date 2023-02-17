import React from "react";



const Aircrafts = () => {
  return (
  <>
     
    <div class="card-group">
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/starships/10.jpg" />
    <div class="card-body">
      <h5 class="card-title">Millennium Falcon</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/starships/12.jpg" />
    <div class="card-body">
      <h5 class="card-title">Card title</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/starships/13.jpg" />
    <div class="card-body">
      <h5 class="card-title">TIE Advanced x1</h5>
      <button type="button" className="btn btn-secondary">Detalles</button>
      <button type="button" className=  " btn btn-outline-danger border-0">
            <i className="far fa-heart"></i>
      </button>
    </div>
  </div>
  <div class="card">
  <img src="https://starwars-visualguide.com/assets/img/starships/15.jpg" />
    <div class="card-body">
      <h5 class="card-title">Executor</h5>
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

export default Aircrafts;