SELECT 
    SUM(network_time_ms) / CAST(
        (SELECT COUNT(request_id) 
         FROM requests 
         WHERE host = 'balancer.test.yandex.ru' 
         AND type = 'RequestReceived'
        ) AS numeric
    ) AS avg_network_time_ms
FROM (
    SELECT 
        EXTRACT(EPOCH FROM (rr.datetime - rs.datetime)) * 1000 AS network_time_ms
    FROM requests rs
    JOIN requests rr ON rs.parent_request_id = rr.request_id AND rs.host = split_part(rr.data, E'\t', 1)
    WHERE rs.type = 'ResponseSent'
    AND rr.type = 'ResponseReceived'
    
    UNION ALL
    
    SELECT 
        EXTRACT(EPOCH FROM (rr.datetime - rs.datetime)) * 1000 AS network_time_ms
    FROM requests rs
    JOIN requests rr ON rs.request_id = rr.parent_request_id AND rs.data = rr.host
    WHERE rs.type = 'RequestSent'
    AND rr.type = 'RequestReceived'
    AND rr.parent_request_id IS NOT NULL
) combined_query;



