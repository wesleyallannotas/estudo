const pause = wait => fn => setTimeout(fn, wait);

pause(600)(() => console.log('Waiting 600ms'))

const wait200 = pause(200);
const wait1000 = pause(100);

wait200(() => console.log('waiting 200ms')) ;
wait1000(() => console.log('Waiting 1s'));