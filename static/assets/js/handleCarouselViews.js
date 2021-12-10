const carouselContainerPc = document.getElementById("carouselPc")
const carouselContainerTablet = document.getElementById("carouselTablet")
const carouselContainerMobile = document.getElementById("carouselMobile")

const carouselContainerPcTop = document.getElementById("carouselPcTop")
const carouselContainerTabletTop = document.getElementById("carouselTabletTop")
const carouselContainerMobileTop = document.getElementById("carouselMobileTop")

const handleCarouselView = () => {
  let width = window.innerWidth

  if (width > 992) {
    console.log("pc")
    carouselContainerPc.classList.remove("d-none")
    carouselContainerMobile.classList.add("d-none")
    carouselContainerTablet.classList.add("d-none")

    carouselContainerPcTop.classList.remove("d-none")
    carouselContainerMobileTop.classList.add("d-none")
    carouselContainerTabletTop.classList.add("d-none")
  } else if (width > 767) {
    console.log("tablet")
    carouselContainerPc.classList.add("d-none")
    carouselContainerMobile.classList.add("d-none")
    carouselContainerTablet.classList.remove("d-none")

    carouselContainerPcTop.classList.add("d-none")
    carouselContainerMobileTop.classList.add("d-none")
    carouselContainerTabletTop.classList.remove("d-none")
  } else {
    console.log("mobile")
    carouselContainerPc.classList.add("d-none")
    carouselContainerMobile.classList.remove("d-none")
    carouselContainerTablet.classList.add("d-none")

    carouselContainerPcTop.classList.add("d-none")
    carouselContainerMobileTop.classList.remove("d-none")
    carouselContainerTabletTop.classList.add("d-none")
  }
}

handleCarouselView()

window.onresize = function(e) {
  handleCarouselView()
}