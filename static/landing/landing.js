"use strict";

var $ = jQuery.noConflict();

/* jQuery easing */
$.extend( $.easing, {
    def: 'easeOutQuad',
    swing: function ( x, t, b, c, d ) {
        return $.easing[ $.easing.def ]( x, t, b, c, d );
    },
    easeOutQuad: function ( x, t, b, c, d ) {
        return -c * ( t /= d ) * ( t - 2 ) + b;
    },
    easeOutQuint: function ( x, t, b, c, d ) {
        return c * ( ( t = t / d - 1 ) * t * t * t * t + 1 ) + b;
    }
} );

/**
 * Riode Object
 */
window.Riode = {};

( function () {

    // Riode Properties
    Riode.$window = $( window );
    Riode.$body = $( document.body );
    Riode.status = '';                                           // Riode Status
    Riode.minDesktopWidth = 992;                                 // Detect desktop screen
    Riode.isIE = navigator.userAgent.indexOf( "Trident" ) >= 0;  // Detect Internet Explorer
    Riode.isEdge = navigator.userAgent.indexOf( "Edge" ) >= 0;   // Detect Edge
    Riode.isMobile = /Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test( navigator.userAgent );   // Detect Mobile
    Riode.defaults = {
        animation: {
            name: 'fadeIn',
            duration: '1.2s',
            delay: '.2s'
        },
        isotope: {
            itemsSelector: '.grid-item',
            layoutMode: 'masonry',
            percentPosition: true,
            masonry: {
                columnWidth: '.grid-space'
            }
        },
        slider: {
            responsiveClass: true,
            navText: [ '<i class="d-icon-angle-left">', '<i class="d-icon-angle-right">' ],
            checkVisible: false,
            items: 1,
            smartSpeed: Riode.isEdge ? 200 : 500,
            autoplaySpeed: Riode.isEdge ? 200 : 1000,
            autoplayTimeout: 10000

        },
        popup: {
            removalDelay: 350,
            callbacks: {
                open: function () {
                    $( 'html' ).css( 'overflow-y', 'hidden' );
                    $( 'body' ).css( 'overflow-x', 'visible' );
                    $( '.mfp-wrap' ).css( 'overflow', 'hidden auto' );
                    $( '.sticky-header.fixed' ).css( 'padding-right', window.innerWidth - document.body.clientWidth );
                },
                close: function () {
                    $( 'html' ).css( 'overflow-y', '' );
                    $( 'body' ).css( 'overflow-x', 'hidden' );
                    $( '.mfp-wrap' ).css( 'overflow', '' );
                    $( '.sticky-header.fixed' ).css( 'padding-right', '' );
                }
            }
        },
        popupPresets: {
            video: {
                type: 'iframe',
                mainClass: "mfp-fade",
                preloader: false,
                closeBtnInside: false
            }
        },
        sliderPresets: {
            'intro-slider': {
                animateIn: 'fadeIn',
                animateOut: 'fadeOut'
            },
            'product-single-carousel': {
                dots: false,
                nav: true,
            },
            'product-gallery-carousel': {
                dots: false,
                nav: true,
                margin: 20,
                items: 1,
                responsive: {
                    576: {
                        items: 2
                    },
                    768: {
                        items: 3
                    }
                },
            },
            'rotate-slider': {
                dots: false,
                nav: true,
                margin: 0,
                items: 1,
                animateIn: '',
                animateOut: ''
            }
        },
        sliderThumbs: {
            margin: 0,
            items: 4,
            dots: false,
            nav: true,
            navText: [ '<i class="fas fa-chevron-left">', '<i class="fas fa-chevron-right">' ]
        },
        stickyContent: {
            minWidth: Riode.minDesktopWidth,
            maxWidth: 20000,
            top: 300,
            hide: false, // hide when it is not sticky.
            max_index: 1060, // maximum z-index of sticky contents
            scrollMode: false
        },
        stickyHeader: {
            // activeScreenWidth: Riode.minDesktopWidth
            activeScreenWidth: 768
        }
    }

	/**
	 * Get jQuery object
	 * @param {string|jQuery} selector
	 */
    Riode.$ = function ( selector ) {
        return selector instanceof jQuery ? selector : $( selector );
    }

	/**
	 * Make a macro task
	 * @param {function} fn
	 * @param {number} delay
	 */
    Riode.call = function ( fn, delay ) {
        setTimeout( fn, delay );
    }

	/**
	 * Get dom element by id
	 * @param {string} id
	 */
    Riode.byId = function ( id ) {
        return document.getElementById( id );
    }

	/**
	 * Get dom elements by tagName
	 * @param {string} tagName
	 * @param {HTMLElement} element this can be omitted.
	 */
    Riode.byTag = function ( tagName, element ) {
        return element ?
            element.getElementsByTagName( tagName ) :
            document.getElementsByTagName( tagName );
    }

	/**
	 * Get dom elements by className
	 * @param {string} className
	 * @param {HTMLElement} element this can be omitted.
	 */
    Riode.byClass = function ( className, element ) {
        return element ?
            element.getElementsByClassName( className ) :
            document.getElementsByClassName( className );
    }

	/**
	 * Set cookie
	 * @param {string} name Cookie name
	 * @param {string} value Cookie value
	 * @param {number} exdays Expire period
	 */
    Riode.setCookie = function ( name, value, exdays ) {
        var date = new Date();
        date.setTime( date.getTime() + ( exdays * 24 * 60 * 60 * 1000 ) );
        document.cookie = name + "=" + value + ";expires=" + date.toUTCString() + ";path=/";
    }

	/**
	 * Get cookie
	 * @param {string} name Cookie name
	 */
    Riode.getCookie = function ( name ) {
        var n = name + "=";
        var ca = document.cookie.split( ';' );
        for ( var i = 0; i < ca.length; ++i ) {
            var c = ca[ i ];
            while ( c.charAt( 0 ) == ' ' ) {
                c = c.substring( 1 );
            }
            if ( c.indexOf( n ) == 0 ) {
                return c.substring( n.length, c.length );
            }
        }
        return "";
    }

	/**
	 * Parse options string to object
	 * @param {string} options
	 */
    Riode.parseOptions = function ( options ) {
        return 'string' == typeof options ?

            JSON.parse( options.replace( /'/g, '"' ).replace( ';', '' ) ) :
            {};
    }

	/**
	 * Parse html template with variables.
	 * @param {string} template
	 * @param {object} vars
	 */
    Riode.parseTemplate = function ( template, vars ) {
        return template.replace( /\{\{(\w+)\}\}/g, function () {
            return vars[ arguments[ 1 ] ];
        } );
    }

    /**
	 * @function requestTimeout
	 * @param {function} fn
	 * @param {number} delay
	 */
    Riode.requestTimeout = function ( fn, delay ) {
        var handler = window.requestAnimationFrame || window.webkitRequestAnimationFrame || window.mozRequestAnimationFrame;
        if ( !handler ) {
            return setTimeout( fn, delay );
        }
        var start, rt = new Object();

        function loop( timestamp ) {
            if ( !start ) {
                start = timestamp;
            }
            var progress = timestamp - start;
            progress >= delay ? fn() : rt.val = handler( loop );
        };

        rt.val = handler( loop );
        return rt;
    }

	/**
	 * @function isOnScreen
	 * @param {HTMLElement} el
	 * @param {number} dx
	 * @param {number} dy
	 */
    Riode.isOnScreen = function ( el, dx, dy ) {
        var a = window.pageXOffset,
            b = window.pageYOffset,
            o = el.getBoundingClientRect(),
            x = o.left + a,
            y = o.top + b,
            ax = typeof dx == 'undefined' ? 0 : dx,
            ay = typeof dy == 'undefined' ? 0 : dy;

        return y + o.height + ay >= b &&
            y <= b + window.innerHeight + ay &&
            x + o.width + ax >= a &&
            x <= a + window.innerWidth + ax;
    }

	/**
	 * @function appear
	 * 
	 * @param {HTMLElement} el
	 * @param {function} fn
	 * @param {object} options
	 */
    Riode.appear = ( function () {
        var checks = [],
            timerId = false,
            one;

        var checkAll = function () {
            for ( var i = checks.length; i--; ) {
                one = checks[ i ];

                if ( Riode.isOnScreen( one.el, one.options.accX, one.options.accY ) ) {
                    typeof $( one.el ).data( 'appear-callback' ) == 'function' && $( one.el ).data( 'appear-callback' ).call( one.el, one.data );
                    one.fn && one.fn.call( one.el, one.data );
                    checks.splice( i, 1 );
                }
            }
        };

        window.addEventListener( 'scroll', checkAll, { passive: true } );
        window.addEventListener( 'resize', checkAll, { passive: true } );
        $( window ).on( 'appear.check', checkAll );

        return function ( el, fn, options ) {
            var settings = {
                data: undefined,
                accX: 0,
                accY: 0
            };

            if ( options ) {
                options.data && ( settings.data = options.data );
                options.accX && ( settings.accX = options.accX );
                options.accY && ( settings.accY = options.accY );
            }

            checks.push( { el: el, fn: fn, options: settings } );
            if ( !timerId ) {
                timerId = Riode.requestTimeout( checkAll, 100 );
            }
        }
    } )();

    var requestAnimFrame =
        window.requestAnimationFrame ||
        window.webkitRequestAnimationFrame ||
        window.mozRequestAnimationFrame ||
        function ( callback ) {
            window.setTimeout( callback, 1000 / 60 );
        };

    function cubicInOut( a ) {
        return .5 > a ? 4 * a * a * a : .5 * Math.pow( 2 * a - 2, 3 ) + 1;
    }

    // parallaxx
    function ParallaxBg( el, options ) {
        this.options = $.extend( {
            speed: 1,
            from: '100%',
            to: '70.5%',
            styleKey: 'width',
            animation: false,
        }, options, Riode.parseOptions( el.getAttribute( 'data-parallax-options' ) ) );
        this.el = el;
        this.flag = true;
        var self = this,
            updateFn = this.update.bind( this ),
            runParallax = function () {
                self.update();
                window.addEventListener( 'resize', updateFn, { passive: true } );
                window.addEventListener( 'scroll', updateFn, { passive: true } );
            };

        runParallax();
    }
    ParallaxBg.prototype.update = function () {
        var self = this,
            top = window.pageYOffset,
            height = window.innerHeight,
            rect = self.el.getBoundingClientRect();

        var value = ( height - rect.top ) * 2 / ( height + rect.height );
        if ( self.options.animation ) {
            if ( 0.4 < value && self.flag ) {
                self.el.classList.add( 'animated' );
                self.flag = false;
            }
            if ( 0.4 > value && !self.flag ) {
                self.el.classList.remove( 'animated' );
                self.flag = true;
            }
        } else {
            $( self.el ).css( self.options.styleKey, 'calc(' + self.options.from + ' + (' + self.options.to + ' - ' + self.options.from + ') * ' + ( value > 1 ? 1 : value ) + ')' );
        }
    }
    Riode.parallaxBg = function ( selector, options ) {
        Riode.$( selector ).each( function () {
            new ParallaxBg( this, options );
        } )
    }

    function ShapeOverlay( el, options ) {
        this.el = el;
        this.$el = $( el );
        this.options = $.extend( {
            layersCount: 4,
            duration: 800,
            delay: 70,
            delayMax: 180,
            fill: '',
            fillMode: '',
            gradient: '',
            color: [ 46, 102, 232 ]
        }, options );
        this.init();
    }

    ShapeOverlay.prototype.init = function () {
        this.isAnimating = false;
        this.status = '';
        this.delays = [];

        this.$el
            .on( 'mouseenter touchstart', this.start.bind( this ) )
            .on( 'mouseleave touchend', this.finish.bind( this ) );

        this.path = this.el.getElementsByClassName( 'overlay-path' );
    }

    ShapeOverlay.prototype.start = function () {
        if ( this.status == '' ) {
            var i, svg = '';
            svg += '<svg class="shape-overlays" viewBox="0 0 100 100" preserveAspectRatio="none"';
            if ( this.options.fill ) {
                svg += ' fill="' + this.options.fill + '"';
            }
            svg += '>' + this.options.gradient;
            for ( i = 0; i < this.options.layersCount; ++i ) {
                svg += '<path opacity="' + ( i + 1 ) / this.options.layersCount + '" class="overlay-path" />';
                this.delays[ i ] = ( Math.sin( 2 * Math.PI * ( Math.random() + i / ( this.options.layersCount ) ) ) + 1 ) / 2 * this.options.delayMax;
            }
            this.$el.append( svg += '</svg>' );

            this.status = 'opening';
            this.timeStart = Date.now();
            this.update();
        }
    }

    ShapeOverlay.prototype.finish = function () {
        if ( this.status == 'opening' ) {
            this.status = 'opening-close';
        } else if ( this.status == 'opened' ) {
            if ( this.options.fillMode == 'onlyshape' ) {
                this.$el.find( '.shape-overlays' ).remove();
                this.status = '';
            } else {
                this.status = 'closing';
                this.timeStart = Date.now();
                this.update();
            }
        }
    }

    ShapeOverlay.prototype.update = function () {
        if ( Date.now() < this.timeStart + this.options.duration + this.options.delay * ( this.options.layersCount - 1 ) + this.options.delayMax ) {
            var self = this;
            requestAnimFrame( function () {
                self.draw();
            } );
        }
        else {
            if ( this.options.fillMode == 'onlyshape' ) {
                this.$el.find( '.shape-overlays' ).remove();
                this.status = '';
            } else {
                if ( this.status == 'opening' ) {
                    this.status = 'opened';
                } else if ( this.status == 'opening-close' ) {
                    this.status = 'closing';
                    this.timeStart = Date.now();
                    this.update();
                } else if ( this.status == 'closing' ) {
                    this.$el.find( '.shape-overlays' ).remove();
                    this.status = '';
                }
            }
            this.isAnimating = false;
        }
    }

    ShapeOverlay.prototype.draw = function () {
        for ( var i = 0; i < this.options.layersCount; ++i ) {
            this.path[ i ].setAttribute( 'd', this.updatePath( Date.now() - this.timeStart - this.options.delay * ( this.status.startsWith( 'opening' ) ? i : this.options.layersCount - i - 1 ) ) );
        }
        this.update();
    }

    ShapeOverlay.prototype.updatePath = function ( time ) {
        var points = [], p, cp, str = '';
        for ( var i = 0; i < this.options.layersCount; ++i ) {
            points[ i ] = cubicInOut( Math.min( Math.max( time - this.delays[ i ], 0 ) / this.options.duration, 1 ) ) * 100
        }

        str += this.status.startsWith( 'opening' ) ? 'M 0 0 V ' + points[ 0 ].toFixed( 2 ) + ' ' : 'M 0 ' + points[ 0 ].toFixed( 2 ) + ' ';
        for ( var i = 0; i < this.options.layersCount - 1; ++i ) {
            p = ( i + 1 ) / ( this.options.layersCount - 1 ) * 100;
            cp = p - ( 1 / ( this.options.layersCount - 1 ) * 100 ) / 2;
            str += 'C ' + cp.toFixed( 2 ) + ' ' + points[ i ].toFixed( 2 ) + ' ' + cp.toFixed( 2 ) + ' ' + points[ i + 1 ].toFixed( 2 ) + ' ' + p.toFixed( 2 ) + ' ' + points[ i + 1 ].toFixed( 2 ) + ' ';
        }
        str += this.status.startsWith( 'opening' ) ? 'V 0 H 0' : 'V 100 H 0';
        return str;
    }

    Riode.shapeOverlay = function ( selector, options ) {
        Riode.$( selector ).each( function () {
            new ShapeOverlay( this, options );
        } )
    }

    function FloatBackground( el, options ) {
        var updateFn = this.update.bind( this );

        this.el = el;
        this.options = $.extend( {
            friction: .03
        }, options );
        this.x2 = this.y2 = this.x = this.y = 0;

        $( window ).on( 'mousemove click', this.moveTo.bind( this ) );
        window.addEventListener( 'resize', updateFn, { passive: true } );
        window.addEventListener( 'scroll', updateFn, { passive: true } );
        this.update();
    }

    FloatBackground.prototype.update = function () {
        var self = this;
        if ( Riode.isOnScreen( this.el ) ) {
            requestAnimFrame( function () {
                self.move();
            } );
        }
    }

    FloatBackground.prototype.moveTo = function ( e ) {
        this.x2 = -0.1 * e.clientX;
        this.y2 = -0.1 * e.clientY;
    }

    FloatBackground.prototype.move = function () {
        this.x += ( this.x2 - this.x ) * this.options.friction;
        this.y += ( this.y2 - this.y ) * this.options.friction;
        this.el.style[ 'background-position' ] = parseInt( this.x ) + 'px ' + parseInt( this.y ) + 'px';
        this.update();
    }

    Riode.floatBackground = function ( selector, options ) {
        Riode.$( selector ).each( function () {
            new FloatBackground( this, options );
        } )
    }

    Riode.scrollTo = function ( arg, duration ) {
        var offset = 0;
        var _duration = typeof duration == 'undefined' ? 600 : duration;
        if ( typeof arg == 'number' ) {
            offset = arg;
        } else {
            offset = Riode.$( arg ).offset().top;
        }
        $( 'html,body' ).stop().animate( { scrollTop: offset }, _duration );
    }

    Riode.floatScrollDefaults = {
        startPos: 'top',
        top: 0,
        speed: 0.1,
        horizontal: false,
        isInsideSVG: true,
        transition: false,
        transitionDelay: 0,
        transitionDuration: 500
    };

    Riode.FloatScrollElement = {
        initScrollFloatElement: function ( $el, opts ) {
            var self = this,
                $window = $( window ),
                minus;

            self.flag = true;

            if ( opts.style ) {
                $el.attr( 'style', opts.style );
            }

            if ( $window.width() > 767 ) {

                // Set Start Position
                if ( opts.startPos == 'none' ) {
                    minus = '';
                    $el.css( {
                        top: opts.top
                    } );
                } else if ( opts.startPos == 'top' ) {
                    $el.css( {
                        top: 0
                    } );
                    minus = '';
                } else {
                    $el.css( {
                        bottom: 0
                    } );
                    minus = '-';
                }

                // Set Transition
                if ( opts.transition ) {
                    $el.css( {
                        transition: 'linear transform ' + opts.transitionDuration + 'ms ' + opts.transitionDelay + 'ms'
                    } );
                }

                // First Load
                self.movement( $el, opts, minus );


                // Scroll
                $window.on( 'scroll', function () {
                    self.movement( $el, opts, minus );
                } );

            }

        },
        movement: function ( $el, opts, minus ) {
            var $window = $( window ),
                scrollTop = $window.scrollTop(),
                elementOffset = $el.offset().top,
                currentElementOffset = ( elementOffset - scrollTop ),
                factor = ( opts.isInsideSVG ) ? 2 : 100,
                elementHeight = $el.innerHeight();

            var scrollPercent = factor * currentElementOffset / ( $window.height() ),
                offset = ( minus + scrollPercent / opts.speed ) * elementHeight / 100,
                firstScrollPercent = factor * ( currentElementOffset + offset ) / ( $window.height() );

            if ( Riode.isOnScreen( $el[ 0 ] ) ) {
                if ( !opts.horizontal ) {

                    if ( this.flag ) {
                        $el.css( {
                            transform: 'translate3d(0, ' + minus + firstScrollPercent / opts.speed + '%, 0)'
                        } );
                        this.flag = false;
                    } else {
                        $el.css( {
                            transform: 'translate3d(0, ' + minus + scrollPercent / opts.speed + '%, 0)'
                        } );
                    }

                } else {

                    $el.css( {
                        transform: 'translate3d(' + minus + scrollPercent / opts.speed + '%, ' + minus + scrollPercent / opts.speed + '%, 0)'
                    } );

                }
            }
        },
        init: function ( selector ) {
            var self = this;
            Riode.$( selector ).each( function () {
                var $this = $( this ),
                    opts;

                opts = $.extend( true, {}, Riode.floatScrollDefaults, Riode.parseOptions( $this.data( 'plugin-options' ) ) );

                self.initScrollFloatElement( $this, opts );
            } );
        }
    };

    /**
	 * @function appearAnimate
	 *
	 * @param {string} selector
	 */
    Riode.appearAnimate = function ( selector ) {
        Riode.$( selector ).each( function () {
            var el = this;
            Riode.appear( el, function () {
                if ( el.classList.contains( 'appear-animate' ) ) {
                    var settings = $.extend( {}, Riode.defaults.animation, Riode.parseOptions( el.getAttribute( 'data-animation-options' ) ) );

                    Riode.call( function () {
                        setTimeout(
                            function () {
                                el.style[ 'animation-duration' ] = settings.duration;
                                el.classList.add( settings.name );
                                el.classList.add( 'appear-animation-visible' );
                            },
                            settings.delay ? Number( settings.delay.slice( 0, -1 ) ) * 1000 : 0
                        );
                    } );
                }
            } );
        } );
    }

    Riode.lazyload = function ( selector, force ) {
        function load() {
            this.setAttribute( 'src', this.getAttribute( 'data-src' ) );
            this.addEventListener( 'load', function () {
                this.style[ 'padding-top' ] = '';
                this.classList.remove( 'lazy-img' );
            } );
        }

        // Lazyload images
        Riode.$( selector ).find( '.lazy-img' ).each( function () {
            if ( 'undefined' != typeof force && force ) {
                load.call( this );
            } else {
                Riode.appear( this, load );
            }
        } )
    }

    /**
     * @function slider
     *
     * @requires OwlCarousel
     */
    Riode.slider = ( function () {
        /**
         * @class Slider
         */
        function Slider( $el, options ) {
            return this.init( $el, options );
        }

        var onInitialize = function ( e ) {
            var i, j, breaks = [ '', '-xs', '-sm', '-md', '-lg', '-xl' ];
            this.classList.remove( 'row' );
            for ( i = 0; i < 6; ++i ) {
                for ( j = 1; j <= 12; ++j ) {
                    this.classList.remove( 'cols' + breaks[ i ] + '-' + j );
                }
            }
            this.classList.remove( 'gutter-no' );
            this.classList.remove( 'gutter-sm' );
            this.classList.remove( 'gutter-lg' );
            if ( this.classList.contains( "animation-slider" ) ) {
                var els = this.children,
                    len = els.length;
                for ( var i = 0; i < len; ++i ) {
                    els[ i ].setAttribute( 'data-index', i + 1 );
                }
            }
        }
        var onInitialized = function ( e ) {
            var els = this.firstElementChild.firstElementChild.children,
                i,
                len = els.length;
            for ( i = 0; i < len; ++i ) {
                if ( !els[ i ].classList.contains( 'active' ) ) {
                    var animates = Riode.byClass( 'appear-animate', els[ i ] ),
                        j;
                    for ( j = animates.length - 1; j >= 0; --j ) {
                        animates[ j ].classList.remove( 'appear-animate' );
                    }
                }
            }

            // Video
            var $el = $( e.currentTarget );
            $el.find( 'video' ).on( 'ended', function () {
                var $this = $( this );
                if ( $this.closest( '.owl-item' ).hasClass( 'active' ) ) {
                    if ( true === $el.data( 'owl.carousel' ).options.autoplay ) {
                        if ( false === $el.data( 'owl.carousel' ).options.loop && ( $el.data().children - 1 ) === $el.find( '.owl-item.active' ).index() ) {
                            this.loop = true;
                            this.play();
                        }
                        $el.trigger( 'next.owl.carousel' );
                        $el.trigger( 'play.owl.autoplay' );
                    } else {
                        this.loop = true;
                        this.play();
                    }
                }
            } );
        }
        var onTranslated = function ( e ) {
            $( window ).trigger( 'appear.check' );

            // Video Play	
            var $el = $( e.currentTarget ),
                $activeVideos = $el.find( '.owl-item.active video' );

            $el.find( '.owl-item:not(.active) video' ).each( function () {
                if ( !this.paused ) {
                    $el.trigger( 'play.owl.autoplay' );
                }
                this.pause();
                this.currentTime = 0;
            } );

            if ( $activeVideos.length ) {
                if ( true === $el.data( 'owl.carousel' ).options.autoplay ) {
                    $el.trigger( 'stop.owl.autoplay' );
                }
                $activeVideos.each( function () {
                    this.paused && this.play();
                } );
            }
        }
        var onSliderInitialized = function ( e ) {
            var self = this,
                $el = $( e.currentTarget );

            // carousel content animation

            $el.find( '.owl-item.active .slide-animate' ).each( function () {
                var $animation_item = $( this ),
                    settings = $.extend( true, {},
                        Riode.defaults.animation,
                        Riode.parseOptions( $animation_item.data( 'animation-options' ) )
                    ),
                    duration = settings.duration,
                    delay = settings.delay,
                    aniName = settings.name;

                $animation_item.css( 'animation-duration', duration );

                var temp = Riode.requestTimeout( function () {
                    $animation_item.addClass( aniName );
                    $animation_item.addClass( 'show-content' );
                }, ( delay ? Number( ( delay ).slice( 0, -1 ) ) * 1000 : 0 ) );

                self.timers.push( temp );
            } );
        }

        var onSliderResized = function ( e ) {
            $( e.currentTarget ).find( '.owl-item.active .slide-animate' ).each( function () {
                var $animation_item = $( this );
                $animation_item.addClass( 'show-content' );
                $animation_item.attr( 'style', '' );
            } );
        }

        var onSliderTranslate = function ( e ) {
            var self = this,
                $el = $( e.currentTarget );
            self.translateFlag = 1;
            self.prev = self.next;
            $el.find( '.owl-item .slide-animate' ).each( function () {
                var $animation_item = $( this ),
                    settings = $.extend( true, {}, Riode.defaults.animation, Riode.parseOptions( $animation_item.data( 'animation-options' ) ) );
                $animation_item.removeClass( settings.name );
            } );
        }

        var onSliderTranslated = function ( e ) {
            var self = this,
                $el = $( e.currentTarget );
            if ( 1 == self.translateFlag ) {
                self.next = $el.find( '.owl-item' ).eq( e.item.index ).children().attr( 'data-index' );
                $el.find( '.show-content' ).removeClass( 'show-content' );
                if ( self.prev != self.next ) {
                    $el.find( '.show-content' ).removeClass( 'show-content' );
                    /* clear all animations that are running. */
                    if ( $el.hasClass( "animation-slider" ) ) {
                        for ( var i = 0; i < self.timers.length; i++ ) {
                            Riode.deleteTimeout( self.timers[ i ] );
                        }
                        self.timers = [];
                    }
                    $el.find( '.owl-item.active .slide-animate' ).each( function () {
                        var $animation_item = $( this ),
                            settings = $.extend( true, {}, Riode.defaults.animation, Riode.parseOptions( $animation_item.data( 'animation-options' ) ) ),
                            duration = settings.duration,
                            delay = settings.delay,
                            aniName = settings.name;

                        $animation_item.css( 'animation-duration', duration );
                        $animation_item.css( 'animation-delay', delay );
                        $animation_item.css( 'transition-property', 'visibility, opacity' );
                        $animation_item.css( 'transition-delay', delay );
                        $animation_item.css( 'transition-duration', duration );
                        $animation_item.addClass( aniName );

                        duration = duration ? duration : '0.75s';
                        $animation_item.addClass( 'show-content' );
                        var temp = Riode.requestTimeout( function () {
                            $animation_item.css( 'transition-property', '' );
                            $animation_item.css( 'transition-delay', '' );
                            $animation_item.css( 'transition-duration', '' );
                            self.timers.splice( self.timers.indexOf( temp ), 1 )
                        }, ( delay ? Number( ( delay ).slice( 0, -1 ) ) * 1000 + Number( ( duration ).slice( 0, -1 ) ) * 500 : Number( ( duration ).slice( 0, -1 ) ) * 500 ) );
                        self.timers.push( temp );
                    } );
                } else {
                    $el.find( '.owl-item' ).eq( e.item.index ).find( '.slide-animate' ).addClass( 'show-content' );
                }
                self.translateFlag = 0;
            }
        }

        // Public Properties

        Slider.zoomImage = function () {
            Riode.zoomImage( this.$element );
        }

        Slider.zoomImageRefresh = function () {
            this.$element.find( 'img' ).each( function () {
                var $this = $( this );

                if ( $.fn.elevateZoom ) {
                    var elevateZoom = $this.data( 'elevateZoom' );
                    if ( typeof elevateZoom !== 'undefined' ) {
                        elevateZoom.refresh();
                    } else {
                        Riode.defaults.zoomImage.zoomContainer = $this.parent();
                        $this.elevateZoom( Riode.defaults.zoomImage );
                    }
                }
            } );
        }

        Riode.defaults.sliderPresets[ 'product-single-carousel' ].onInitialized = Riode.defaults.sliderPresets[ 'product-gallery-carousel' ].onInitialized = Slider.zoomImage;
        Riode.defaults.sliderPresets[ 'product-single-carousel' ].onRefreshed = Riode.defaults.sliderPresets[ 'product-gallery-carousel' ].onRefreshed = Slider.zoomImageRefresh;

        Slider.prototype.init = function ( $el, options ) {
            this.timers = [];
            this.translateFlag = 0;
            this.prev = 1;
            this.next = 1;

            Riode.lazyload( $el, true );

            var classes = $el.attr( 'class' ).split( ' ' ),
                settings = $.extend( true, {}, Riode.defaults.slider );

            // extend preset options
            classes.forEach( function ( className ) {
                var preset = Riode.defaults.sliderPresets[ className ];
                preset && $.extend( true, settings, preset );
            } );

            var $videos = $el.find( 'video' );
            $videos.each( function () {
                this.loop = false;
            } );

            // extend user options
            $.extend( true, settings, Riode.parseOptions( $el.attr( 'data-owl-options' ) ), options );

            onSliderInitialized = onSliderInitialized.bind( this );
            onSliderTranslate = onSliderTranslate.bind( this );
            onSliderTranslated = onSliderTranslated.bind( this );

            // init
            $el.on( 'initialize.owl.carousel', onInitialize )
                .on( 'initialized.owl.carousel', onInitialized )
                .on( 'translated.owl.carousel', onTranslated );

            // if animation slider
            $el.hasClass( 'animation-slider' ) &&
                $el.on( 'initialized.owl.carousel', onSliderInitialized )
                    .on( 'resized.owl.carousel', onSliderResized )
                    .on( 'translate.owl.carousel', onSliderTranslate )
                    .on( 'translated.owl.carousel', onSliderTranslated );

            $el.owlCarousel( settings );
        }

        return function ( selector, options ) {
            Riode.$( selector ).each( function () {
                var $this = $( this );

                Riode.call( function () {
                    new Slider( $this, options );
                } );
            } );
        }
    } )();

	/**
	 * @function popup
	 * @requires magnificPopup
	 * @params {object} options
	 * @params {string|undefined} preset
	 */
    Riode.popup = function ( options, preset ) {
        var mpInstance = $.magnificPopup.instance,
            opt = $.extend( true, {},
                Riode.defaults.popup,
                ( 'undefined' != typeof preset ) ? Riode.defaults.popupPresets[ preset ] : {},
                options
            );

        // if something is already opened ( except login popup )
        if ( mpInstance.isOpen && mpInstance.content ) {
            mpInstance.close(); // close current
            setTimeout( function () { // and open new after a moment
                $.magnificPopup.open( opt );
            }, 500 );
        } else {
            $.magnificPopup.open( opt ); // if nothing is opened, open new
        }
    }

    /**
	 * @function initPopups
	 */
    Riode.initPopups = function () {

        Riode.$body.on( 'click', '.btn-iframe', function ( e ) {
            e.preventDefault();
            Riode.popup( {
                items: {
                    src: '<video src="' + $( e.currentTarget ).attr( 'href' ) + '" autoplay loop controls>',
                    type: "inline"
                },
                mainClass: "mfp-video-popup"
            }, "video" )
        } )


    }

    /**
	 * @function stickyContent
	 * Init Sticky Content
	 * @param {string, Object} selector
	 * @param {Object} settings
	 */
    Riode.stickyContent = function ( selector, settings ) {
        var $stickyContents = Riode.$( selector ),
            options = $.extend( {}, Riode.defaults.stickyContent, settings ),
            scrollPos = window.pageYOffset;

        if ( 0 == $stickyContents.length ) return;

        var setTopOffset = function ( $item ) {
            var offset = 0,
                index = 0;
            $( '.sticky-content.fixed.fix-top' ).each( function () {
                offset += $( this )[ 0 ].offsetHeight;
                index++;
            } );
            $item.data( 'offset-top', offset );
            $item.data( 'z-index', options.max_index - index );
        }

        var setBottomOffset = function ( $item ) {
            var offset = 0,
                index = 0;
            $( '.sticky-content.fixed.fix-bottom' ).each( function () {
                offset += $( this )[ 0 ].offsetHeight;
                index++;
            } );
            $item.data( 'offset-bottom', offset );
            $item.data( 'z-index', options.max_index - index );
        }

        var wrapStickyContent = function ( $item, height ) {
            if ( window.innerWidth >= options.minWidth && window.innerWidth <= options.maxWidth ) {
                $item.wrap( '<div class="sticky-content-wrapper"></div>' );
                $item.parent().css( 'height', height + 'px' );
                $item.data( 'is-wrap', true );
            }
        }

        var initStickyContent = function () {
            $stickyContents.each( function ( index ) {
                var $item = $( this );
                if ( !$item.data( 'is-wrap' ) ) {
                    var height = $item.removeClass( 'fixed' ).outerHeight( true ), top;
                    top = $item.offset().top + height;

                    // if sticky header has category dropdown, increase top
                    if ( $item.hasClass( 'has-dropdown' ) ) {
                        var $box = $item.find( '.category-dropdown .dropdown-box' );

                        if ( $box.length ) {
                            top += $box[ 0 ].offsetHeight;
                        }
                    }

                    $item.data( 'top', top );
                    wrapStickyContent( $item, height );
                } else {
                    if ( window.innerWidth < options.minWidth || window.innerWidth >= options.maxWidth ) {
                        $item.unwrap( '.sticky-content-wrapper' );
                        $item.data( 'is-wrap', false );
                    }
                }
            } );
        }

        var refreshStickyContent = function ( e ) {
            if ( e && !e.isTrusted ) return;
            $stickyContents.each( function ( index ) {
                var $item = $( this ),
                    showContent = true;
                if ( options.scrollMode ) {
                    showContent = scrollPos > window.pageYOffset;
                    scrollPos = window.pageYOffset;
                }
                if ( window.pageYOffset > ( false == options.top ? $item.data( 'top' ) : options.top ) && window.innerWidth >= options.minWidth && window.innerWidth <= options.maxWidth ) {
                    if ( $item.hasClass( 'fix-top' ) ) {
                        if ( undefined === $item.data( 'offset-top' ) ) {
                            setTopOffset( $item );
                        }
                        $item.css( 'margin-top', $item.data( 'offset-top' ) + 'px' );
                    } else if ( $item.hasClass( 'fix-bottom' ) ) {
                        if ( undefined === $item.data( 'offset-bottom' ) ) {
                            setBottomOffset( $item );
                        }
                        $item.css( 'margin-bottom', $item.data( 'offset-bottom' ) + 'px' );
                    }
                    $item.css( 'z-index', $item.data( 'z-index' ) );
                    if ( options.scrollMode ) {
                        if ( ( showContent && $item.hasClass( 'fix-top' ) ) || ( !showContent && $item.hasClass( 'fix-bottom' ) ) ) {
                            $item.addClass( 'fixed' );
                        } else {
                            $item.removeClass( 'fixed' );
                            $item.css( 'margin', '' );
                        }
                    } else {
                        $item.addClass( 'fixed' );
                    }
                    options.hide && $item.parent( '.sticky-content-wrapper' ).css( 'display', '' );
                } else {
                    $item.removeClass( 'fixed' );
                    $item.css( 'margin-top', '' );
                    $item.css( 'margin-bottom', '' );
                    options.hide && $item.parent( '.sticky-content-wrapper' ).css( 'display', 'none' );
                }
            } );
        }

        var resizeStickyContent = function ( e ) {
            $stickyContents.removeData( 'offset-top' )
                .removeData( 'offset-bottom' )
                .removeClass( 'fixed' )
                .css( 'margin', '' )
                .css( 'z-index', '' );

            Riode.call( function () {
                initStickyContent();
                refreshStickyContent();
            } );
        }

        setTimeout( initStickyContent, 550 );
        setTimeout( refreshStickyContent, 600 );

        Riode.call( function () {
            window.addEventListener( 'scroll', refreshStickyContent, { passive: true } );
            Riode.$window.on( 'resize', resizeStickyContent );
        }, 700 );
    }

    /**
	 * @function initScrollTopButton
	 */
    Riode.initScrollTopButton = function () {
        // register scroll top button

        var domScrollTop = Riode.byId( 'scroll-top' );

        if ( domScrollTop ) {
            domScrollTop.addEventListener( 'click', function ( e ) {
                $( 'html, body' ).animate( { scrollTop: 0 }, 600 );
                e.preventDefault();
            } );

            var refreshScrollTop = function () {
                if ( window.pageYOffset > 400 ) {
                    domScrollTop.classList.add( 'show' );
                } else {
                    domScrollTop.classList.remove( 'show' );
                }
            }

            Riode.call( refreshScrollTop, 500 );
            window.addEventListener( 'scroll', refreshScrollTop, { passive: true } );
        }
    }

    /**
	 * @function isotopes
	 *
	 * @requires isotope,imagesLoaded
	 * @param {string} selector
	 * @param {object} options
	 */
    Riode.isotopes = function ( selector, options ) {
        if ( typeof imagesLoaded === 'function' && $.fn.isotope ) {
            var self = this;

            Riode.$( selector ).each( function () {
                var $this = $( this ),
                    settings = $.extend( true, {},
                        Riode.defaults.isotope,
                        Riode.parseOptions( $this.attr( 'data-grid-options' ) ),
                        options ? options : {}
                    );

                Riode.lazyload( $this );
                $this.imagesLoaded( function () {
                    settings.customInitHeight && $this.height( $this.height() );
                    settings.customDelay && Riode.call( function () {
                        $this.isotope( settings );
                    }, parseInt( settings.customDelay ) );

                    $this.isotope( settings );
                } )
            } );
        }
    }

	/**
	 * @function initNavFilter
	 *
	 * @requires isotope
	 * @param {string} selector
	 */
    Riode.initNavFilter = function ( selector ) {
        if ( $.fn.isotope ) {
            Riode.$( selector ).on( 'click', function ( e ) {
                var $this = $( this ),
                    filterValue = $this.attr( 'data-filter' ),
                    filterTarget = $this.parent().parent().attr( 'data-target' );
                ( filterTarget ? $( filterTarget ) : $( '.grid' ) )
                    .isotope( { filter: filterValue } )
                    .isotope( 'on', 'arrangeComplete', function () {
                        Riode.$window.trigger( 'appear.check' );
                    } );
                $this.parent().siblings().children().removeClass( 'active' );
                $this.addClass( 'active' );
                e.preventDefault();
            } );
        }
    }

    /**
	 * @function playableVideo
	 *
	 * @param {string} selector
	 */
    Riode.playableVideo = function ( selector ) {
        $( selector + ' .video-play' ).on( 'click', function ( e ) {
            var $video = $( this ).closest( selector );
            if ( $video.hasClass( 'playing' ) ) {
                $video.removeClass( 'playing' )
                    .addClass( 'paused' )
                    .find( 'video' )[ 0 ].pause();
            } else {
                $video.removeClass( 'paused' )
                    .addClass( 'playing' )
                    .find( 'video' )[ 0 ].play();
            }
            e.preventDefault();
        } );
        $( selector + ' video' ).on( 'ended', function () {
            $( this ).closest( selector ).removeClass( 'playing' );
        } );
    }

    $( window ).on( 'riode_complete', function () {
        Riode.floatBackground( '.float-bg' ); // issue : if visible
        // Riode.floatSVG( '.expshape1', { speed: 5 } );
        // Riode.floatSVG( '.expshape2', { speed: 4 } );
        // Riode.floatEl( '.float-el' );
        // Riode.particles( '.particle1' );
        // Riode.particles( '.particle2', {
        //     space: 20,
        //     count: 13
        // } );
        Riode.shapeOverlay( '.shape-overlay', {
            fill: 'url(#bg-gradient)',
            gradient: '<defs><linearGradient id="bg-gradient" y2="100%"><stop offset="0" stop-color="#08c"/><stop offset="100%" stop-color="#5349ff"/></linearGradient></defs>'
        } );
        $( '.demos .appear-animate, .features .appear-animate' ).each( function () {
            this.setAttribute( 'data-animation-options', "{'name':'fadeInUpShorter','duration':'.5s','delay':'" + parseInt( Math.random() * 3 ) / 10 + "s'}" );
        } );

        Riode.$body.on( 'click', '.main-nav a, .mobile-menu a, .scroll-to', function ( e ) {
            var link = e.currentTarget, hash = link.hash ? link.hash : link.slice( link.lastIndexOf( '#' ) );
            if ( hash.startsWith( '#' ) ) {
                $( '.mobile-menu-overlay' ).click();
                Riode.scrollTo( hash );
                e.preventDefault();
            }
        } );



        Riode.lazyload( document.body );
        Riode.playableVideo( '.video-banner' );
        Riode.parallaxBg( '.parallax-effect' );
        Riode.FloatScrollElement.init( '.scroll-float-el' );
    } );

    // Initialize Method while document is interactive
    Riode.initLayout = function () {
        Riode.isotopes( '.grid:not(.grid-float)' );
    }

    Riode.initMenu = function () {
        // setup menu
        $( '.menu li' ).each( function () {
            if ( this.lastElementChild && (
                this.lastElementChild.tagName === 'UL' ||
                this.lastElementChild.classList.contains( 'megamenu' ) )
            ) {
                this.classList.add( 'submenu' );
            }
        } );

        $( '.main-nav .megamenu, .main-nav .submenu > ul' ).each( function () {
            var $this = $( this ),
                left = $this.offset().left,
                outerWidth = $this.outerWidth(),
                offset = ( left + outerWidth ) - ( window.innerWidth - 20 );
            if ( $this.closest( 'li' ).hasClass( 'submenu-container' ) ) {
                var winWidth = $( window ).innerWidth();
                if ( winWidth <= 1180 ) {
                    $this.css( 'width', winWidth );
                    outerWidth = $this.outerWidth();
                }
                $this.css( 'margin-left', ( ( winWidth - outerWidth ) / 2 - left ) );
            }
            else {
                if ( offset >= 0 && left > 20 ) {
                    $this.css( 'margin-left', '-=' + offset );
                }
            }
        } );

        // calc megamenu position
        Riode.$window.on( 'resize', function () {
            $( '.main-nav .megamenu, .main-nav .submenu > ul' ).each( function () {
                var $this = $( this ),
                    left = $this.offset().left,
                    outerWidth = $this.outerWidth(),
                    offset = ( left + outerWidth ) - ( window.innerWidth - 20 );
                if ( $this.closest( 'li' ).hasClass( 'submenu-container' ) ) {
                    var winWidth = $( window ).innerWidth();
                    if ( winWidth <= 1180 ) {
                        $this.css( 'width', winWidth );
                        outerWidth = $this.outerWidth();
                    }
                    $this.css( 'margin-left', 0 );
                    left = $this.offset().left;
                    $this.css( 'margin-left', ( ( winWidth - outerWidth ) / 2 - left ) );
                } else {
                    if ( offset >= 0 && left > 20 ) {
                        $this.css( 'margin-left', '-=' + offset );
                    }
                }
            } );
        } );
    }

    Riode.initMobileMenu = function () {
        function showMobileMenu() {
            Riode.$body.addClass( 'mmenu-active' );
        };
        function hideMobileMenu() {
            Riode.$body.removeClass( 'mmenu-active' );
        };

        $( '.mobile-menu li, .toggle-menu li' ).each( function () {
            if ( this.lastElementChild && (
                this.lastElementChild.tagName === 'UL' ||
                this.lastElementChild.classList.contains( 'megamenu' ) )
            ) {
                var span = document.createElement( 'span' );
                span.className = "toggle-btn";
                this.firstElementChild.appendChild( span );
            }
        } );
        $( '.mobile-menu-toggle' ).on( 'click', showMobileMenu );
        $( '.mobile-menu-overlay' ).on( 'click', hideMobileMenu );
        $( '.mobile-menu-close' ).on( 'click', hideMobileMenu );
        Riode.$window.on( 'resize', hideMobileMenu );
    }
    // Initialize Method after document has been loaded
    Riode.init = function () {
        Riode.appearAnimate( '.appear-animate' );                               // Runs appear animations
        Riode.slider( '.owl-carousel' );                                        // Initialize slider
        Riode.stickyContent( '.product-sticky-content, .sticky-header', { top: false } );       // Initialize sticky content
        Riode.initScrollTopButton();                                            // Initialize scroll top button.
        Riode.initNavFilter( '.nav-filters .nav-filter' );                      // Initialize navigation filters for blog, products
        Riode.initPopups();                                                     // Initialize popup
        Riode.initMenu();                                                       // Initialize menu
        Riode.initMobileMenu();                                                 // Initialize mobile menu
        Riode.status = 'complete';
    }

    window.onload = function () {
        Riode.status = 'loaded';
        Riode.$body.addClass( 'loaded' );
        Riode.$window.trigger( 'riode_load' );

        Riode.call( Riode.initLayout );
        Riode.call( Riode.init );
        Riode.$window.trigger( 'riode_complete' );
    }
} )( jQuery );