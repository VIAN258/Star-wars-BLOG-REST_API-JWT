import React, { useState, useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import { Context } from "../store/appContext";


export const Signup = () => {
    const { store, actions } = useContext(Context);
    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const navigate = useNavigate();

    const sendData = async(event) => {
        event.preventDefault();
        const user = {
            "name": username, 
            "email": email, 
            "password": password
        }
        const response = await actions.register(user);
        if (response ["code"] == 0 ) navigate("/");
        else alert(response ["response"])
    };

    return (
        <React.Fragment>
            <div className="container signup w-50 mt-2">
                <h1 className="text-center display-6">SIGNUP</h1>
                <form onSubmit={sendData}>
                    <div className="mb-3">
                        <label className="form-label">Username</label>
                        <input
                            className="form-control"
                            placeholder="Please set your Username"
                            type="text"
                            value={username}
                            onChange={(event) => setUsername(event.target.value.trim())}
                        />
                    </div>
                    <div className="mb-3">
                        <label
                            className="form-label">Email address
                        </label>
                        <input
                            className="form-control"
                            placeholder="Please enter your email"
                            type="email"
                            value={email}
                            onChange={(event) => setEmail(event.target.value)}
                        />
                    </div>
                    <div className="mb-3">
                        <label className="form-label">Password</label>
                        <input
                            className="form-control"
                            placeholder="Please enter your password"
                            type="password"
                            value={password}
                            onChange={(event) => setPassword(event.target.value.trim())}
                        />
                    </div>
                    <div className="text-center">
                        <input className="btn btn-primary w-25" type="submit" value="Signup" />
                    </div>
                </form>
            </div>
        </React.Fragment>
    );
};