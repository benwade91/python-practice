let tl = gsap.timeline({
    scrollTrigger: {
        trigger: 'home',
        start: '0%',
        end: '50%',
        scrub: 1
    }
})

let tl2 = gsap.timeline({
    scrollTrigger: {
        trigger: 'home',
        start: '0%',
        end: '30%',
        scrub: 1
    }
})

let tl3 = gsap.timeline({
    scrollTrigger: {
        trigger: '.home',
        start: '0%',
        end: '300%',
        scrub: 1,
        pin: true,
        pinSpacing: false
    }
})

tl.fromTo(".sliding-text", {y:0}, {y:-400});
tl2.fromTo(".logo", {scale: 4}, {scale: 1, top: '2rem', left: '4rem', x: '10%'})