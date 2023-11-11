const workSection = document.querySelector(".section-work-data");

const workSectionObserve = (entries) => {
    const [entry] = entries;
    if (!entry.isIntersecting) return;
    console.log(entries);


    const counterNum = document.querySelectorAll(".counter-numbers");
    // console.log(counterNum);
    const speed = 200;

    counterNum.forEach((curNumber) => {
        const updateNumber = () => {
            const targetNumber = parseInt(curNumber.dataset.number);
            // console.log(targetNumber);
            const initialNumber = parseInt(curNumber.innerText);
            // console.log(initialNumber);
            const incrementNumber = Math.trunc(targetNumber / speed);
            // i am adding the value to the main number
            // console.log(incrementNumber);

            if (initialNumber < targetNumber) {
                curNumber.innerText = `${initialNumber + incrementNumber}+`;
                setTimeout(updateNumber, 10);
            } else {
                curNumber.innerText = `${targetNumber}+`;
            }

        };
        updateNumber();
    });
};

const workSecObserver = new IntersectionObserver(workSectionObserve, {
    root: null,
    threshold: 0,
});

workSecObserver.observe(workSection);