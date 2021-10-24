let tl = gsap.timeline({
    scrollTrigger: {
        trigger: '.home',
        start: '0%',
        end: '80%',
        scrub: 1
    }
})

let tl2 = gsap.timeline({
    scrollTrigger: {
        trigger: '.home',
        start: '0%',
        end: '100%',
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

let tl4 = gsap.timeline({
    scrollTrigger: {
        trigger: 'home',
        start: '0%',
        end: '20%',
        scrub: 1
    }
})

tl.fromTo(".sliding-text", {y:0}, {y:-200});
tl2.fromTo(".logo", {scale: 8}, {scale: 1, top: '2.5rem', left: '5rem', x: '10%'})
tl4.fromTo(".honeybee", {left: '20%'}, {left: '100%', top: '10%', opacity: 0})