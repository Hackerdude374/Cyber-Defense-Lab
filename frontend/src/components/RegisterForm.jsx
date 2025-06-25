import { useState } from "react";

export default function RegisterForm() {
  const [form, setForm] = useState({ username: "", password: "", role: "red" });

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("http://localhost:5000/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(form)
    });
    const data = await res.json();
    console.log(data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input placeholder="Username" onChange={(e) => setForm({ ...form, username: e.target.value })} />
      <input placeholder="Password" type="password" onChange={(e) => setForm({ ...form, password: e.target.value })} />
      <select onChange={(e) => setForm({ ...form, role: e.target.value })}>
        <option value="red">Red Team</option>
        <option value="blue">Blue Team</option>
      </select>
      <button type="submit">Register</button>
    </form>
  );
}