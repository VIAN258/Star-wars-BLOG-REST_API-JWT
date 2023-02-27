
const URL= "https://3001-vian258-starwarsblogres-osz01sn5ake.ws-us88.gitpod.io"


const getState = ({ getStore, getActions, setStore }) => {
	return {
		store: {
			message: null,
			demo: [
				{
					title: "FIRST",
					background: "white",
					initial: "white"
				},
				{
					title: "SECOND",
					background: "white",
					initial: "white"
				}
			],
			favorites : []
		},
		actions: {
			addFavorites: (name) => {
				const store = getStore ()
				const tmp = store.favorites
				tmp.push(name)
				setStore ({favorites: tmp})
			},
			removeFavorites: (name) => {
				const store = getStore ();
				const tmp = store.favorites.filter(item => item !== name);
				setStore ({favorites: tmp});
			},
			// Use getActions to call a function within a fuction
			exampleFunction: () => {
				getActions().changeColor(0, "green");
			},

			getMessage: async () => {
				try{
					// fetching data from the backend
					const resp = await fetch(process.env.BACKEND_URL + "/api/hello")
					const data = await resp.json()
					setStore({ message: data.message })
					// don't forget to return something, that is how the async resolves
					return data;
				}catch(error){
					console.log("Error loading message from backend", error)
				}
			},
			changeColor: (index, color) => {
				//get the store
				const store = getStore();

				//we have to loop the entire demo array to look for the respective index
				//and change its color
				const demo = store.demo.map((elm, i) => {
					if (i === index) elm.background = color;
					return elm;
				});

				//reset the global store
				setStore({ demo: demo });
			},
			register: async(user)=> {
               const response = await fetch(URL + "/api/signup",{
				crossDomain: true,
				method: "POST",
				mode: "cors",
				headers: {
					"Content-Type": "application/json",
				},
				referrerPolicy: "no-referrer",
				body: JSON.stringify(user),
					}).then((res) =>res.json())
				console.log(response)
					return response
			},
			login: async(email, password)=> {
				const response = await fetch(URL + "/api/login",{
				 crossDomain: true,
				 method: "POST",
				 mode: "cors",
				 headers: {
					 "Content-Type": "application/json",
				 },
				 referrerPolicy: "no-referrer",
				 body: JSON.stringify({"email": email, "password": password}),
					 }).then((res) =>res.json())
				 console.log(response)
					 return response
			 },
		}
	};
};

export default getState;
