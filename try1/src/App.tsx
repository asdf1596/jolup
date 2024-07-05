import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
    const [data, setData] = useState<{ val?: string }>({});
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState<string | null>(null);

    useEffect(() => {
        const fetchData = () => {
            fetch("/users")
                .then((response) => {
                    if (!response.ok) {
                        throw new Error(
                            `HTTP error! status: ${response.status}`
                        );
                    }
                    return response.json();
                })
                .then((data) => {
                    console.log(data);
                    setData(data);
                    setLoading(false);
                })
                .catch((err) => {
                    setError(err.message);
                    setLoading(false);
                });
        };

        fetchData(); // 컴포넌트가 마운트될 때 즉시 데이터를 가져옴
        const interval = setInterval(fetchData, 1000); // 1초마다 fetchData 함수 호출

        return () => clearInterval(interval); // 컴포넌트 언마운트 시 인터벌 정리
    }, []);

    return (
        <div className="App">
            <div>
                {loading ? (
                    <p>Loading...</p>
                ) : error ? (
                    <p>Error: {error}</p>
                ) : (
                    <p>{data.val}</p>
                )}
            </div>
        </div>
    );
}

export default App;
