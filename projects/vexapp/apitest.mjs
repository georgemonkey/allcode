import RobotEvents from "robotevents";

const re = new RobotEvents({
  apiKey: "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiIzIiwianRpIjoiMmQ4OGMzYjJlMjVkMjhiNWM5OWJlZDVhOTcyYWY3MmNiMWU4MjY0ZmUxNzAxZTQzNDJjNGMwNGVkM2ZmN2NmODU2MzQwOTE0OTM3NWUyNTUiLCJpYXQiOjE3NDk0NDE3MDAuNDM1ODU0LCJuYmYiOjE3NDk0NDE3MDAuNDM1ODU4LCJleHAiOjI2OTYxMjY1MDAuNDMwMTc3Miwic3ViIjoiMTQ2NzkzIiwic2NvcGVzIjpbXX0.b9HBwr2qAuuQy_vALAo5-MNVcweb2Lcfa1s7PhGC1FiAFRmD6MY0zlLe1YpjeRTJJ_p5W9e9W2b2sTiQyyA5uQOTxUVgQWueBSEgVpX3hNwrkvSEUsTIUeYOTKERxYmQkPeY_DZgNL1oBf4ec9T7xe4YH86TjgRVViT4VKIl9TOoU4opF4gozRfy5_D-TVp0BfAZ6Sae14V4HpRC7RKd0bvj3Qe19eyFXGrO3CWeMFcvC0HhZSdgLTOU7A0RQZiXp3mPFA7E35OTPiGMJpeIxpekguPhkezuuLfWQmy5kKdRtHJtPOISH2kb8QWNhmegntpdwpyPERx34zi-uCqy3cbdnlvNmZl4hYGI8HXPYB2gQscq9g0s2Xv4jUiDDmDQCEARifLs7KTLoZnBZnB8mp6BQkqUwEsZRAmDHGmqFOK8Y2hQqJxWN8ziLlYkgUQPACTXnMMzVUZeiBxFasM57WztOKW1ec1l8EBUtnHHI3-eSvrGM5DX4ilFzxiZsH9VW69SNBr9K3i-Si_kUE9ZX_c-VgYmtHmPOHYjEl23RB9YjwoWBl2o9W0SOivL-oWmJof4HKvxUJZHhVAdokfQk08fEi6GAI4y6-QdLJKvOIjMeVpMPQcf8p_v4Q2vQa5OvI-sSDUm0nxhYNd1oW3muflIZ3fS1RAjUIBY4zyNR3w",
});

async function getEvents() {
  const events = await re.getEvents({ season: "2023" });
  console.log(events);
}

getEvents();