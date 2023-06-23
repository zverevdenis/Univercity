export default function({ $axios }, inject ) {
    $axios.create = ({
        headers: {
            common: {
                Accept: 'text/plain, */*',
                'Content-Type': 'application/json'
            }
        }
    })
    $axios.baseURL = "http://localhost:5023";

    $axios.onRequest(config => {
        config.context = config.context || {};
        config.context.startTimeMs = Date.now();
    });

    $axios.onResponse(response => {
        response.context = response.context || {};
    });

    $axios.onError(error => {
        if (
            error.response &&
            (error.response.status === 400 || error.response.status === 500)
        ) {
            if (process.server) {
                console.error("process.server", error);
            } else {
            }
        }
        try {
            const endTimeMs = Date.now();
            const duration = endTimeMs - error.config.context.startTimeMs;
            const errorMessage = {
                level: "error",
                url: error.config.url,
                duration: `${duration} ms`
            };
            console.log(errorMessage);
        } catch {
            // TO DO
        }
    });
}