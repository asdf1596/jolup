import React, { useEffect, useState } from "react";
import "./App.css";

interface User {
    val: string;
}

function App() {
    const [pre, setPre] = useState<{ val?: string }>({});
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
                    setPre(data);
                    setLoading(false);
                })
                .catch((err) => {
                    setError(err.message);
                    setLoading(false);
                });
        };

        // 초기 데이터 로드
        fetchData();

        // 1초마다 데이터 갱신
        const interval = setInterval(fetchData, 1000);

        // 컴포넌트 언마운트 시 인터벌 정리
        return () => clearInterval(interval);
    }, []);

    return (
        <div className="App">
            <div>
                {loading ? (
                    <p>loading...</p>
                ) : error ? (
                    <p>Error: {error}</p>
                ) : (
                    <p>{pre.val}</p>
                )}
            </div>
        </div>
    );
}

export default App;
