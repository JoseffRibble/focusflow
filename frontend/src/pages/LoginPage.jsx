import React, { useState } from "react";
import axios from "../utils/axiosInstance";
import { useNavigate } from "react-router-dom";

export default function LoginPage() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleLogin = async (e) => {
    e.preventDefault();
    setError("");

    try {
      const response = await axios.post(
        "/login/",
        {
          email,
          password,
        },
        { skip401Redirect: true },
      );

      console.log("[DEBUG] Login response:", response.data);
      // Store the token in localStorage
      localStorage.setItem("token", response.data.access);

      // Redirect to tasks page
      navigate("/tasks");
    } catch (err) {
      console.error("[DEBUG] Login failed:", err.response?.data || err.message);
      setError("Invalid credentials");
    }
  };

  return (
    <div>
      <h2>Login</h2>
      <form onSubmit={handleLogin}>
        <div>
          <label>Email: </label>
          <input
            data-testid="email-input"
            type="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Password: </label>
          <input
            data-testid="password-input"
            type="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" data-testid="login-button">
          Login
        </button>

        {error && (
          <p style={{ color: "red" }} data-testid="login-error">
            {error}
          </p>
        )}
      </form>
    </div>
  );
}
