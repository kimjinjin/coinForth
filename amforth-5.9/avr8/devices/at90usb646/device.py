# Partname:  AT90USB646
# generated automatically, do not edit
MCUREGS = {
	'WDTCSR': '&96',
	  'WDTCSR_WDIF': '$80',
	  'WDTCSR_WDIE': '$40',
	  'WDTCSR_WDP': '$27',
	  'WDTCSR_WDCE': '$10',
	  'WDTCSR_WDE': '$08',
	'PORTA': '&34',
	'DDRA': '&33',
	'PINA': '&32',
	'PORTB': '&37',
	'DDRB': '&36',
	'PINB': '&35',
	'PORTC': '&40',
	'DDRC': '&39',
	'PINC': '&38',
	'PORTD': '&43',
	'DDRD': '&42',
	'PIND': '&41',
	'PORTE': '&46',
	'DDRE': '&45',
	'PINE': '&44',
	'PORTF': '&49',
	'DDRF': '&48',
	'PINF': '&47',
	'SREG': '&95',
	  'SREG_I': '$80',
	  'SREG_T': '$40',
	  'SREG_H': '$20',
	  'SREG_S': '$10',
	  'SREG_V': '$08',
	  'SREG_N': '$04',
	  'SREG_Z': '$02',
	  'SREG_C': '$01',
	'SP': '&93',
	'MCUCR': '&85',
	  'MCUCR_JTD': '$80',
	  'MCUCR_PUD': '$10',
	  'MCUCR_IVSEL': '$02',
	  'MCUCR_IVCE': '$01',
	'MCUSR': '&84',
	  'MCUSR_JTRF': '$10',
	  'MCUSR_WDRF': '$08',
	  'MCUSR_BORF': '$04',
	  'MCUSR_EXTRF': '$02',
	  'MCUSR_PORF': '$01',
	'XMCRA': '&116',
	  'XMCRA_SRE': '$80',
	  'XMCRA_SRL': '$70',
	  'XMCRA_SRW1': '$0C',
	  'XMCRA_SRW0': '$03',
	'XMCRB': '&117',
	  'XMCRB_XMBK': '$80',
	  'XMCRB_XMM': '$07',
	'OSCCAL': '&102',
	'CLKPR': '&97',
	  'CLKPR_CLKPCE': '$80',
	  'CLKPR_CLKPS': '$0F',
	'SMCR': '&83',
	  'SMCR_SM': '$0E',
	  'SMCR_SE': '$01',
	'EIND': '&92',
	'RAMPZ': '&91',
	'GPIOR2': '&75',
	  'GPIOR2_GPIOR': '$FF',
	'GPIOR1': '&74',
	  'GPIOR1_GPIOR': '$FF',
	'GPIOR0': '&62',
	  'GPIOR0_GPIOR07': '$80',
	  'GPIOR0_GPIOR06': '$40',
	  'GPIOR0_GPIOR05': '$20',
	  'GPIOR0_GPIOR04': '$10',
	  'GPIOR0_GPIOR03': '$08',
	  'GPIOR0_GPIOR02': '$04',
	  'GPIOR0_GPIOR01': '$02',
	  'GPIOR0_GPIOR00': '$01',
	'PRR1': '&101',
	  'PRR1_PRUSB': '$80',
	  'PRR1_PRTIM3': '$08',
	  'PRR1_PRUSART1': '$01',
	'PRR0': '&100',
	  'PRR0_PRTWI': '$80',
	  'PRR0_PRTIM2': '$40',
	  'PRR0_PRTIM0': '$20',
	  'PRR0_PRTIM1': '$08',
	  'PRR0_PRSPI': '$04',
	  'PRR0_PRADC': '$01',
	'TWAMR': '&189',
	  'TWAMR_TWAM': '$FE',
	'TWBR': '&184',
	'TWCR': '&188',
	  'TWCR_TWINT': '$80',
	  'TWCR_TWEA': '$40',
	  'TWCR_TWSTA': '$20',
	  'TWCR_TWSTO': '$10',
	  'TWCR_TWWC': '$08',
	  'TWCR_TWEN': '$04',
	  'TWCR_TWIE': '$01',
	'TWSR': '&185',
	  'TWSR_TWS': '$F8',
	  'TWSR_TWPS': '$03',
	'TWDR': '&187',
	'TWAR': '&186',
	  'TWAR_TWA': '$FE',
	  'TWAR_TWGCE': '$01',
	'SPCR': '&76',
	  'SPCR_SPIE': '$80',
	  'SPCR_SPE': '$40',
	  'SPCR_DORD': '$20',
	  'SPCR_MSTR': '$10',
	  'SPCR_CPOL': '$08',
	  'SPCR_CPHA': '$04',
	  'SPCR_SPR': '$03',
	'SPSR': '&77',
	  'SPSR_SPIF': '$80',
	  'SPSR_WCOL': '$40',
	  'SPSR_SPI2X': '$01',
	'SPDR': '&78',
	'UDR1': '&206',
	'UCSR1A': '&200',
	  'UCSR1A_RXC1': '$80',
	  'UCSR1A_TXC1': '$40',
	  'UCSR1A_UDRE1': '$20',
	  'UCSR1A_FE1': '$10',
	  'UCSR1A_DOR1': '$08',
	  'UCSR1A_UPE1': '$04',
	  'UCSR1A_U2X1': '$02',
	  'UCSR1A_MPCM1': '$01',
	'UCSR1B': '&201',
	  'UCSR1B_RXCIE1': '$80',
	  'UCSR1B_TXCIE1': '$40',
	  'UCSR1B_UDRIE1': '$20',
	  'UCSR1B_RXEN1': '$10',
	  'UCSR1B_TXEN1': '$08',
	  'UCSR1B_UCSZ12': '$04',
	  'UCSR1B_RXB81': '$02',
	  'UCSR1B_TXB81': '$01',
	'UCSR1C': '&202',
	  'UCSR1C_UMSEL1': '$C0',
	  'UCSR1C_UPM1': '$30',
	  'UCSR1C_USBS1': '$08',
	  'UCSR1C_UCSZ1': '$06',
	  'UCSR1C_UCPOL1': '$01',
	'UBRR1': '&204',
	'UEINT': '&244',
	'UEBCHX': '&243',
	'UEBCLX': '&242',
	'UEDATX': '&241',
	'UEIENX': '&240',
	  'UEIENX_FLERRE': '$80',
	  'UEIENX_NAKINE': '$40',
	  'UEIENX_NAKOUTE': '$10',
	  'UEIENX_RXSTPE': '$08',
	  'UEIENX_RXOUTE': '$04',
	  'UEIENX_STALLEDE': '$02',
	  'UEIENX_TXINE': '$01',
	'UESTA1X': '&239',
	  'UESTA1X_CTRLDIR': '$04',
	  'UESTA1X_CURRBK': '$03',
	'UESTA0X': '&238',
	  'UESTA0X_CFGOK': '$80',
	  'UESTA0X_OVERFI': '$40',
	  'UESTA0X_UNDERFI': '$20',
	  'UESTA0X_DTSEQ': '$0C',
	  'UESTA0X_NBUSYBK': '$03',
	'UECFG1X': '&237',
	  'UECFG1X_EPSIZE': '$70',
	  'UECFG1X_EPBK': '$0C',
	  'UECFG1X_ALLOC': '$02',
	'UECFG0X': '&236',
	  'UECFG0X_EPTYPE': '$C0',
	  'UECFG0X_EPDIR': '$01',
	'UECONX': '&235',
	  'UECONX_STALLRQ': '$20',
	  'UECONX_STALLRQC': '$10',
	  'UECONX_RSTDT': '$08',
	  'UECONX_EPEN': '$01',
	'UERST': '&234',
	  'UERST_EPRST': '$7F',
	'UENUM': '&233',
	'UEINTX': '&232',
	  'UEINTX_FIFOCON': '$80',
	  'UEINTX_NAKINI': '$40',
	  'UEINTX_RWAL': '$20',
	  'UEINTX_NAKOUTI': '$10',
	  'UEINTX_RXSTPI': '$08',
	  'UEINTX_RXOUTI': '$04',
	  'UEINTX_STALLEDI': '$02',
	  'UEINTX_TXINI': '$01',
	'UDMFN': '&230',
	  'UDMFN_FNCERR': '$10',
	'UDFNUM': '&228',
	'UDADDR': '&227',
	  'UDADDR_ADDEN': '$80',
	  'UDADDR_UADD': '$7F',
	'UDIEN': '&226',
	  'UDIEN_UPRSME': '$40',
	  'UDIEN_EORSME': '$20',
	  'UDIEN_WAKEUPE': '$10',
	  'UDIEN_EORSTE': '$08',
	  'UDIEN_SOFE': '$04',
	  'UDIEN_SUSPE': '$01',
	'UDINT': '&225',
	  'UDINT_UPRSMI': '$40',
	  'UDINT_EORSMI': '$20',
	  'UDINT_WAKEUPI': '$10',
	  'UDINT_EORSTI': '$08',
	  'UDINT_SOFI': '$04',
	  'UDINT_SUSPI': '$01',
	'UDCON': '&224',
	  'UDCON_LSM': '$04',
	  'UDCON_RMWKUP': '$02',
	  'UDCON_DETACH': '$01',
	'OTGINT': '&223',
	  'OTGINT_STOI': '$20',
	  'OTGINT_HNPERRI': '$10',
	  'OTGINT_ROLEEXI': '$08',
	  'OTGINT_BCERRI': '$04',
	  'OTGINT_VBERRI': '$02',
	  'OTGINT_SRPI': '$01',
	'OTGIEN': '&222',
	  'OTGIEN_STOE': '$20',
	  'OTGIEN_HNPERRE': '$10',
	  'OTGIEN_ROLEEXE': '$08',
	  'OTGIEN_BCERRE': '$04',
	  'OTGIEN_VBERRE': '$02',
	  'OTGIEN_SRPE': '$01',
	'OTGCON': '&221',
	  'OTGCON_HNPREQ': '$20',
	  'OTGCON_SRPREQ': '$10',
	  'OTGCON_SRPSEL': '$08',
	  'OTGCON_VBUSHWC': '$04',
	  'OTGCON_VBUSREQ': '$02',
	  'OTGCON_VBUSRQC': '$01',
	'OTGTCON': '&249',
	  'OTGTCON_OTGTCON_7': '$80',
	  'OTGTCON_PAGE': '$60',
	  'OTGTCON_VALUE_2': '$07',
	'USBINT': '&218',
	  'USBINT_IDTI': '$02',
	  'USBINT_VBUSTI': '$01',
	'USBSTA': '&217',
	  'USBSTA_SPEED': '$08',
	  'USBSTA_ID': '$02',
	  'USBSTA_VBUS': '$01',
	'USBCON': '&216',
	  'USBCON_USBE': '$80',
	  'USBCON_HOST': '$40',
	  'USBCON_FRZCLK': '$20',
	  'USBCON_OTGPADE': '$10',
	  'USBCON_IDTE': '$02',
	  'USBCON_VBUSTE': '$01',
	'UHWCON': '&215',
	  'UHWCON_UIMOD': '$80',
	  'UHWCON_UIDE': '$40',
	  'UHWCON_UVCONE': '$10',
	  'UHWCON_UVREGE': '$01',
	'UPERRX': '&245',
	  'UPERRX_COUNTER': '$60',
	  'UPERRX_CRC16': '$10',
	  'UPERRX_TIMEOUT': '$08',
	  'UPERRX_PID': '$04',
	  'UPERRX_DATAPID': '$02',
	  'UPERRX_DATATGL': '$01',
	'UPINT': '&248',
	'UPBCHX': '&247',
	'UPBCLX': '&246',
	'UPDATX': '&175',
	'UPIENX': '&174',
	  'UPIENX_FLERRE': '$80',
	  'UPIENX_NAKEDE': '$40',
	  'UPIENX_PERRE': '$10',
	  'UPIENX_TXSTPE': '$08',
	  'UPIENX_TXOUTE': '$04',
	  'UPIENX_RXSTALLE': '$02',
	  'UPIENX_RXINE': '$01',
	'UPCFG2X': '&173',
	'UPSTAX': '&172',
	  'UPSTAX_CFGOK': '$80',
	  'UPSTAX_OVERFI': '$40',
	  'UPSTAX_UNDERFI': '$20',
	  'UPSTAX_DTSEQ': '$0C',
	  'UPSTAX_NBUSYK': '$03',
	'UPCFG1X': '&171',
	  'UPCFG1X_PSIZE': '$70',
	  'UPCFG1X_PBK': '$0C',
	  'UPCFG1X_ALLOC': '$02',
	'UPCFG0X': '&170',
	  'UPCFG0X_PTYPE': '$C0',
	  'UPCFG0X_PTOKEN': '$30',
	  'UPCFG0X_PEPNUM': '$0F',
	'UPCONX': '&169',
	  'UPCONX_PFREEZE': '$40',
	  'UPCONX_INMODE': '$20',
	  'UPCONX_RSTDT': '$08',
	  'UPCONX_PEN': '$01',
	'UPRST': '&168',
	  'UPRST_PRST': '$7F',
	'UPNUM': '&167',
	'UPINTX': '&166',
	  'UPINTX_FIFOCON': '$80',
	  'UPINTX_NAKEDI': '$40',
	  'UPINTX_RWAL': '$20',
	  'UPINTX_PERRI': '$10',
	  'UPINTX_TXSTPI': '$08',
	  'UPINTX_TXOUTI': '$04',
	  'UPINTX_RXSTALLI': '$02',
	  'UPINTX_RXINI': '$01',
	'UPINRQX': '&165',
	'UHFLEN': '&164',
	'UHFNUM': '&162',
	'UHADDR': '&161',
	'UHIEN': '&160',
	  'UHIEN_HWUPE': '$40',
	  'UHIEN_HSOFE': '$20',
	  'UHIEN_RXRSME': '$10',
	  'UHIEN_RSMEDE': '$08',
	  'UHIEN_RSTE': '$04',
	  'UHIEN_DDISCE': '$02',
	  'UHIEN_DCONNE': '$01',
	'UHINT': '&159',
	  'UHINT_UHUPI': '$40',
	  'UHINT_HSOFI': '$20',
	  'UHINT_RXRSMI': '$10',
	  'UHINT_RSMEDI': '$08',
	  'UHINT_RSTI': '$04',
	  'UHINT_DDISCI': '$02',
	  'UHINT_DCONNI': '$01',
	'UHCON': '&158',
	  'UHCON_RESUME': '$04',
	  'UHCON_RESET': '$02',
	  'UHCON_SOFEN': '$01',
	'SPMCSR': '&87',
	  'SPMCSR_SPMIE': '$80',
	  'SPMCSR_RWWSB': '$40',
	  'SPMCSR_SIGRD': '$20',
	  'SPMCSR_RWWSRE': '$10',
	  'SPMCSR_BLBSET': '$08',
	  'SPMCSR_PGWRT': '$04',
	  'SPMCSR_PGERS': '$02',
	  'SPMCSR_SPMEN': '$01',
	'EEAR': '&65',
	'EEDR': '&64',
	'EECR': '&63',
	  'EECR_EEPM': '$30',
	  'EECR_EERIE': '$08',
	  'EECR_EEMPE': '$04',
	  'EECR_EEPE': '$02',
	  'EECR_EERE': '$01',
	'OCR0B': '&72',
	'OCR0A': '&71',
	'TCNT0': '&70',
	'TCCR0B': '&69',
	  'TCCR0B_FOC0A': '$80',
	  'TCCR0B_FOC0B': '$40',
	  'TCCR0B_WGM02': '$08',
	  'TCCR0B_CS0': '$07',
	'TCCR0A': '&68',
	  'TCCR0A_COM0A': '$C0',
	  'TCCR0A_COM0B': '$30',
	  'TCCR0A_WGM0': '$03',
	'TIMSK0': '&110',
	  'TIMSK0_OCIE0B': '$04',
	  'TIMSK0_OCIE0A': '$02',
	  'TIMSK0_TOIE0': '$01',
	'TIFR0': '&53',
	  'TIFR0_OCF0B': '$04',
	  'TIFR0_OCF0A': '$02',
	  'TIFR0_TOV0': '$01',
	'GTCCR': '&67',
	  'GTCCR_TSM': '$80',
	  'GTCCR_PSRSYNC': '$01',
	'TIMSK2': '&112',
	  'TIMSK2_OCIE2B': '$04',
	  'TIMSK2_OCIE2A': '$02',
	  'TIMSK2_TOIE2': '$01',
	'TIFR2': '&55',
	  'TIFR2_OCF2B': '$04',
	  'TIFR2_OCF2A': '$02',
	  'TIFR2_TOV2': '$01',
	'TCCR2A': '&176',
	  'TCCR2A_COM2A': '$C0',
	  'TCCR2A_COM2B': '$30',
	  'TCCR2A_WGM2': '$03',
	'TCCR2B': '&177',
	  'TCCR2B_FOC2A': '$80',
	  'TCCR2B_FOC2B': '$40',
	  'TCCR2B_WGM22': '$08',
	  'TCCR2B_CS2': '$07',
	'TCNT2': '&178',
	'OCR2B': '&180',
	'OCR2A': '&179',
	'ASSR': '&182',
	  'ASSR_EXCLK': '$40',
	  'ASSR_AS2': '$20',
	  'ASSR_TCN2UB': '$10',
	  'ASSR_OCR2AUB': '$08',
	  'ASSR_OCR2BUB': '$04',
	  'ASSR_TCR2AUB': '$02',
	  'ASSR_TCR2BUB': '$01',
	'TCCR3A': '&144',
	  'TCCR3A_COM3A': '$C0',
	  'TCCR3A_COM3B': '$30',
	  'TCCR3A_COM3C': '$0C',
	  'TCCR3A_WGM3': '$03',
	'TCCR3B': '&145',
	  'TCCR3B_ICNC3': '$80',
	  'TCCR3B_ICES3': '$40',
	  'TCCR3B_WGM3': '$18',
	  'TCCR3B_CS3': '$07',
	'TCCR3C': '&146',
	  'TCCR3C_FOC3A': '$80',
	  'TCCR3C_FOC3B': '$40',
	  'TCCR3C_FOC3C': '$20',
	'TCNT3': '&148',
	'OCR3A': '&152',
	'OCR3B': '&154',
	'OCR3C': '&156',
	'ICR3': '&150',
	'TIMSK3': '&113',
	  'TIMSK3_ICIE3': '$20',
	  'TIMSK3_OCIE3C': '$08',
	  'TIMSK3_OCIE3B': '$04',
	  'TIMSK3_OCIE3A': '$02',
	  'TIMSK3_TOIE3': '$01',
	'TIFR3': '&56',
	  'TIFR3_ICF3': '$20',
	  'TIFR3_OCF3C': '$08',
	  'TIFR3_OCF3B': '$04',
	  'TIFR3_OCF3A': '$02',
	  'TIFR3_TOV3': '$01',
	'TCCR1A': '&128',
	  'TCCR1A_COM1A': '$C0',
	  'TCCR1A_COM1B': '$30',
	  'TCCR1A_COM1C': '$0C',
	  'TCCR1A_WGM1': '$03',
	'TCCR1B': '&129',
	  'TCCR1B_ICNC1': '$80',
	  'TCCR1B_ICES1': '$40',
	  'TCCR1B_WGM1': '$18',
	  'TCCR1B_CS1': '$07',
	'TCCR1C': '&130',
	  'TCCR1C_FOC1A': '$80',
	  'TCCR1C_FOC1B': '$40',
	  'TCCR1C_FOC1C': '$20',
	'TCNT1': '&132',
	'OCR1A': '&136',
	'OCR1B': '&138',
	'OCR1C': '&140',
	'ICR1': '&134',
	'TIMSK1': '&111',
	  'TIMSK1_ICIE1': '$20',
	  'TIMSK1_OCIE1C': '$08',
	  'TIMSK1_OCIE1B': '$04',
	  'TIMSK1_OCIE1A': '$02',
	  'TIMSK1_TOIE1': '$01',
	'TIFR1': '&54',
	  'TIFR1_ICF1': '$20',
	  'TIFR1_OCF1C': '$08',
	  'TIFR1_OCF1B': '$04',
	  'TIFR1_OCF1A': '$02',
	  'TIFR1_TOV1': '$01',
	'OCDR': '&81',
	'EICRA': '&105',
	  'EICRA_ISC3': '$C0',
	  'EICRA_ISC2': '$30',
	  'EICRA_ISC1': '$0C',
	  'EICRA_ISC0': '$03',
	'EICRB': '&106',
	  'EICRB_ISC7': '$C0',
	  'EICRB_ISC6': '$30',
	  'EICRB_ISC5': '$0C',
	  'EICRB_ISC4': '$03',
	'EIMSK': '&61',
	  'EIMSK_INT': '$FF',
	'EIFR': '&60',
	  'EIFR_INTF': '$FF',
	'PCMSK0': '&107',
	'PCIFR': '&59',
	  'PCIFR_PCIF0': '$01',
	'PCICR': '&104',
	  'PCICR_PCIE0': '$01',
	'ADMUX': '&124',
	  'ADMUX_REFS': '$C0',
	  'ADMUX_ADLAR': '$20',
	  'ADMUX_MUX': '$1F',
	'ADCSRA': '&122',
	  'ADCSRA_ADEN': '$80',
	  'ADCSRA_ADSC': '$40',
	  'ADCSRA_ADATE': '$20',
	  'ADCSRA_ADIF': '$10',
	  'ADCSRA_ADIE': '$08',
	  'ADCSRA_ADPS': '$07',
	'ADC': '&120',
	'ADCSRB': '&123',
	  'ADCSRB_ADHSM': '$80',
	  'ADCSRB_ADTS': '$07',
	'DIDR0': '&126',
	  'DIDR0_ADC7D': '$80',
	  'DIDR0_ADC6D': '$40',
	  'DIDR0_ADC5D': '$20',
	  'DIDR0_ADC4D': '$10',
	  'DIDR0_ADC3D': '$08',
	  'DIDR0_ADC2D': '$04',
	  'DIDR0_ADC1D': '$02',
	  'DIDR0_ADC0D': '$01',
	'ACSR': '&80',
	  'ACSR_ACD': '$80',
	  'ACSR_ACBG': '$40',
	  'ACSR_ACO': '$20',
	  'ACSR_ACI': '$10',
	  'ACSR_ACIE': '$08',
	  'ACSR_ACIC': '$04',
	  'ACSR_ACIS': '$03',
	'DIDR1': '&127',
	  'DIDR1_AIN1D': '$02',
	  'DIDR1_AIN0D': '$01',
	'PLLCSR': '&73',
	  'PLLCSR_PLLP': '$1C',
	  'PLLCSR_PLLE': '$02',
	  'PLLCSR_PLOCK': '$01',
	'INT0Addr': '2',
	'INT1Addr': '4',
	'INT2Addr': '6',
	'INT3Addr': '8',
	'INT4Addr': '10',
	'INT5Addr': '12',
	'INT6Addr': '14',
	'INT7Addr': '16',
	'PCINT0Addr': '18',
	'USB_GENAddr': '20',
	'USB_COMAddr': '22',
	'WDTAddr': '24',
	'TIMER2_COMPAAddr': '26',
	'TIMER2_COMPBAddr': '28',
	'TIMER2_OVFAddr': '30',
	'TIMER1_CAPTAddr': '32',
	'TIMER1_COMPAAddr': '34',
	'TIMER1_COMPBAddr': '36',
	'TIMER1_COMPCAddr': '38',
	'TIMER1_OVFAddr': '40',
	'TIMER0_COMPAAddr': '42',
	'TIMER0_COMPBAddr': '44',
	'TIMER0_OVFAddr': '46',
	'SPI__STCAddr': '48',
	'USART1__RXAddr': '50',
	'USART1__UDREAddr': '52',
	'USART1__TXAddr': '54',
	'ANALOG_COMPAddr': '56',
	'ADCAddr': '58',
	'EE_READYAddr': '60',
	'TIMER3_CAPTAddr': '62',
	'TIMER3_COMPAAddr': '64',
	'TIMER3_COMPBAddr': '66',
	'TIMER3_COMPCAddr': '68',
	'TIMER3_OVFAddr': '70',
	'TWIAddr': '72',
	'SPM_READYAddr': '74'
}