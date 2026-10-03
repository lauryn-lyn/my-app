"use client";

import { useEffect, useState } from "react";

type Service = {
  id: number;
  title: string;
  description: string;
  category: string;
  barter_target: string;
  created_at: string;
  username: string;
};

export default function Page() {
  const [services, setServices] = useState<Service[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/api/services/")
      .then((response) => response.json())
      .then((data) => {
        setServices(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching services:", error);
        setLoading(false);
      });
  }, []);

  return (
    <main style={{ padding: "40px" }}>
      <h1>Service Exchange</h1>

      {loading ? (
        <p>Loading services...</p>
      ) : services.length === 0 ? (
        <p>No services available yet.</p>
      ) : (
        services.map((service) => (
          <div key={service.id} style={{ marginBottom: "20px" }}>
            <h2>{service.title}</h2>
            <p>{service.description}</p>
            <p>Category: {service.category}</p>
            <p>Wants in exchange: {service.barter_target}</p>
            <p>Posted by: {service.username}</p>
          </div>
        ))
      )}
    </main>
  );
}
