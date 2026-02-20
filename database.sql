--
-- PostgreSQL database dump
--

\restrict TV1GW9zAc9Xb8ewMW3ZvsZfZz4BB7az7OI8n9m44djdsUzt3GINb96lz00OUmEt

-- Dumped from database version 16.11 (Ubuntu 16.11-0ubuntu0.24.04.1)
-- Dumped by pg_dump version 16.11 (Ubuntu 16.11-0ubuntu0.24.04.1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: balance_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.balance_model (
    idn integer NOT NULL,
    u_idn integer,
    amount character varying(50),
    is_benefit smallint,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE public.balance_model OWNER TO postgres;

--
-- Name: balance_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.balance_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.balance_model_idn_seq OWNER TO postgres;

--
-- Name: balance_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.balance_model_idn_seq OWNED BY public.balance_model.idn;


--
-- Name: errors_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.errors_model (
    idn integer NOT NULL,
    u_idn integer,
    description text,
    error_pl character varying(255),
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE public.errors_model OWNER TO postgres;

--
-- Name: errors_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.errors_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.errors_model_idn_seq OWNER TO postgres;

--
-- Name: errors_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.errors_model_idn_seq OWNED BY public.errors_model.idn;


--
-- Name: essay_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.essay_model (
    idn integer NOT NULL,
    video text,
    cost double precision,
    section integer,
    participated integer,
    active smallint DEFAULT 1,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now()),
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    created_by integer,
    updated_by integer,
    deleted_by integer,
    deleted smallint DEFAULT 0
);


ALTER TABLE public.essay_model OWNER TO postgres;

--
-- Name: essay_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.essay_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.essay_model_idn_seq OWNER TO postgres;

--
-- Name: essay_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.essay_model_idn_seq OWNED BY public.essay_model.idn;


--
-- Name: essay_user_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.essay_user_model (
    idn integer NOT NULL,
    essay_idn integer,
    u_idn integer,
    paid smallint,
    proof text,
    amount double precision,
    in_process smallint,
    deadline timestamp with time zone,
    starting_date timestamp with time zone,
    message_id character varying(255),
    message_id2 character varying(255),
    done_by integer,
    active smallint,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE public.essay_user_model OWNER TO postgres;

--
-- Name: essay_user_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.essay_user_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.essay_user_model_idn_seq OWNER TO postgres;

--
-- Name: essay_user_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.essay_user_model_idn_seq OWNED BY public.essay_user_model.idn;


--
-- Name: essentials_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.essentials_model (
    idn integer NOT NULL,
    key character varying(250),
    val character varying(250),
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE public.essentials_model OWNER TO postgres;

--
-- Name: essentials_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.essentials_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.essentials_model_idn_seq OWNER TO postgres;

--
-- Name: essentials_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.essentials_model_idn_seq OWNED BY public.essentials_model.idn;


--
-- Name: event_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.event_model (
    idn integer NOT NULL,
    name character varying(255),
    video text,
    cost double precision,
    section integer,
    participated integer,
    starting_date timestamp with time zone,
    active smallint DEFAULT 1,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now()),
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone,
    created_by integer,
    updated_by integer,
    deleted_by integer,
    deleted smallint DEFAULT 0
);


ALTER TABLE public.event_model OWNER TO postgres;

--
-- Name: event_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.event_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.event_model_idn_seq OWNER TO postgres;

--
-- Name: event_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.event_model_idn_seq OWNED BY public.event_model.idn;


--
-- Name: event_user_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.event_user_model (
    idn integer NOT NULL,
    event_idn integer,
    u_idn integer,
    paid smallint,
    proof text,
    amount double precision,
    in_process smallint,
    deadline timestamp with time zone,
    message_id character varying(255),
    message_id2 character varying(255),
    done_by integer,
    active smallint,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE public.event_user_model OWNER TO postgres;

--
-- Name: event_user_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.event_user_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.event_user_model_idn_seq OWNER TO postgres;

--
-- Name: event_user_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.event_user_model_idn_seq OWNED BY public.event_user_model.idn;


--
-- Name: history_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.history_model (
    idn integer NOT NULL,
    u_idn integer,
    message text,
    message_id text,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE public.history_model OWNER TO postgres;

--
-- Name: history_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.history_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.history_model_idn_seq OWNER TO postgres;

--
-- Name: history_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.history_model_idn_seq OWNED BY public.history_model.idn;


--
-- Name: tg_group_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tg_group_model (
    idn integer NOT NULL,
    group_id text,
    status smallint,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE public.tg_group_model OWNER TO postgres;

--
-- Name: tg_group_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tg_group_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tg_group_model_idn_seq OWNER TO postgres;

--
-- Name: tg_group_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tg_group_model_idn_seq OWNED BY public.tg_group_model.idn;


--
-- Name: tg_group_section_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.tg_group_section_model (
    idn integer NOT NULL,
    group_idn integer,
    section_id integer,
    type_connected smallint,
    status smallint,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE public.tg_group_section_model OWNER TO postgres;

--
-- Name: tg_group_section_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.tg_group_section_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.tg_group_section_model_idn_seq OWNER TO postgres;

--
-- Name: tg_group_section_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.tg_group_section_model_idn_seq OWNED BY public.tg_group_section_model.idn;


--
-- Name: transaction_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.transaction_model (
    idn integer NOT NULL,
    balance_idn integer,
    created_by integer,
    amount character varying(50),
    proof text,
    for_what character varying(100),
    for_what_idn integer,
    is_benefit smallint,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now())
);


ALTER TABLE public.transaction_model OWNER TO postgres;

--
-- Name: transaction_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.transaction_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.transaction_model_idn_seq OWNER TO postgres;

--
-- Name: transaction_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.transaction_model_idn_seq OWNED BY public.transaction_model.idn;


--
-- Name: user_model; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.user_model (
    idn integer NOT NULL,
    chat_id character varying(255),
    id_name character varying(255),
    phone_number character varying(20),
    tg_username character varying(64),
    tg_first_name character varying(64),
    tg_last_name character varying(64),
    name character varying(64),
    age integer,
    used bigint DEFAULT 1,
    role smallint DEFAULT 0,
    lang character varying(4),
    active smallint DEFAULT 1,
    log_in smallint,
    deleted smallint DEFAULT 0,
    created_at timestamp with time zone DEFAULT timezone('Asia/Tashkent'::text, now()),
    updated_at timestamp with time zone,
    deleted_at timestamp with time zone
);


ALTER TABLE public.user_model OWNER TO postgres;

--
-- Name: user_model_idn_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.user_model_idn_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER SEQUENCE public.user_model_idn_seq OWNER TO postgres;

--
-- Name: user_model_idn_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.user_model_idn_seq OWNED BY public.user_model.idn;


--
-- Name: balance_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.balance_model ALTER COLUMN idn SET DEFAULT nextval('public.balance_model_idn_seq'::regclass);


--
-- Name: errors_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.errors_model ALTER COLUMN idn SET DEFAULT nextval('public.errors_model_idn_seq'::regclass);


--
-- Name: essay_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.essay_model ALTER COLUMN idn SET DEFAULT nextval('public.essay_model_idn_seq'::regclass);


--
-- Name: essay_user_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.essay_user_model ALTER COLUMN idn SET DEFAULT nextval('public.essay_user_model_idn_seq'::regclass);


--
-- Name: essentials_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.essentials_model ALTER COLUMN idn SET DEFAULT nextval('public.essentials_model_idn_seq'::regclass);


--
-- Name: event_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_model ALTER COLUMN idn SET DEFAULT nextval('public.event_model_idn_seq'::regclass);


--
-- Name: event_user_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_user_model ALTER COLUMN idn SET DEFAULT nextval('public.event_user_model_idn_seq'::regclass);


--
-- Name: history_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_model ALTER COLUMN idn SET DEFAULT nextval('public.history_model_idn_seq'::regclass);


--
-- Name: tg_group_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tg_group_model ALTER COLUMN idn SET DEFAULT nextval('public.tg_group_model_idn_seq'::regclass);


--
-- Name: tg_group_section_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tg_group_section_model ALTER COLUMN idn SET DEFAULT nextval('public.tg_group_section_model_idn_seq'::regclass);


--
-- Name: transaction_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaction_model ALTER COLUMN idn SET DEFAULT nextval('public.transaction_model_idn_seq'::regclass);


--
-- Name: user_model idn; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_model ALTER COLUMN idn SET DEFAULT nextval('public.user_model_idn_seq'::regclass);


--
-- Data for Name: balance_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.balance_model (idn, u_idn, amount, is_benefit, created_at) FROM stdin;
1	1	0	1	2026-02-05 00:37:05.903955+00
\.


--
-- Data for Name: errors_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.errors_model (idn, u_idn, description, error_pl, created_at) FROM stdin;
\.


--
-- Data for Name: essay_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.essay_model (idn, video, cost, section, participated, active, created_at, updated_at, deleted_at, created_by, updated_by, deleted_by, deleted) FROM stdin;
1	BAACAgQAAxkBAAMraYKDh5AKzdexP1C7VztpKvStghsAAhMKAALhTh1QrEkjgmOstgY4BA	100000	31	\N	1	2026-02-04 19:24:47.447767+00	\N	\N	\N	\N	\N	0
\.


--
-- Data for Name: essay_user_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.essay_user_model (idn, essay_idn, u_idn, paid, proof, amount, in_process, deadline, starting_date, message_id, message_id2, done_by, active, created_at) FROM stdin;
1	1	1	0	AgACAgIAAxkBAAIEtGmExDK3EXFKEXyc1G7HB8cElQABcgAC-xNrG5NLIEimARA5A9zR2wEAAwIAA3kAAzgE	100000	1	\N	2026-02-10 15:00:00+00	237	239	\N	1	2026-02-05 16:24:19.304014+00
\.


--
-- Data for Name: essentials_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.essentials_model (idn, key, val, created_at) FROM stdin;
1	credit_card	5614 6822 1973 4029	2026-02-05 00:24:47.437649+00
\.


--
-- Data for Name: event_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.event_model (idn, name, video, cost, section, participated, starting_date, active, created_at, updated_at, deleted_at, created_by, updated_by, deleted_by, deleted) FROM stdin;
\.


--
-- Data for Name: event_user_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.event_user_model (idn, event_idn, u_idn, paid, proof, amount, in_process, deadline, message_id, message_id2, done_by, active, created_at) FROM stdin;
\.


--
-- Data for Name: history_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.history_model (idn, u_idn, message, message_id, created_at) FROM stdin;
1	1	Services 📣	915	2026-02-05 00:37:09.071108+00
2	1	Essay 📝	917	2026-02-05 00:37:11.588208+00
3	1	None	919	2026-02-05 00:37:15.000648+00
4	1	Championship 🏆	921	2026-02-05 00:37:16.71261+00
5	1	Services 📣	926	2026-02-05 06:25:49.937205+00
6	1	Championship 🏆	928	2026-02-05 08:17:18.724817+00
7	1	Essay 📝	930	2026-02-05 08:17:21.088187+00
8	1	None	932	2026-02-05 08:17:23.66763+00
9	1	Services 📣	940	2026-02-05 15:12:06.538133+00
10	1	Championship 🏆	942	2026-02-05 15:12:08.33531+00
11	1	Essay 📝	944	2026-02-05 15:12:10.731271+00
12	1	None	946	2026-02-05 15:12:13.115913+00
13	1	Services 📣	951	2026-02-05 16:43:16.080622+00
14	1	Championship 🏆	953	2026-02-05 19:41:14.752726+00
15	1	Essay 📝	955	2026-02-05 19:41:16.100866+00
16	1	None	957	2026-02-05 19:41:18.919848+00
17	1	Services 📣	1084	2026-02-05 21:13:58.428845+00
18	1	Championship 🏆	1093	2026-02-05 21:14:01.003099+00
19	1	Essay 📝	1095	2026-02-05 21:14:02.426023+00
20	1	book_essay	1097	2026-02-05 21:14:04.362049+00
21	1	2026-02-12	1098	2026-02-05 21:14:06.839192+00
22	1	2026-02-12 15:00	1098	2026-02-05 21:14:08.11154+00
23	1	Services 📣	1142	2026-02-05 21:20:39.113272+00
24	1	Essay 📝	1144	2026-02-05 21:20:40.241364+00
25	1	None	1146	2026-02-05 21:20:41.565768+00
26	1	Services 📣	1152	2026-02-05 21:22:46.467743+00
27	1	Essay 📝	1154	2026-02-05 21:22:47.646714+00
28	1	book_essay	1156	2026-02-05 21:22:49.190804+00
29	1	2026-02-10	1157	2026-02-05 21:22:50.717069+00
30	1	2026-02-10 15:00	1157	2026-02-05 21:22:51.744813+00
31	1	cancel_essay	1157	2026-02-05 21:22:53.050671+00
32	1	Great, now you should pay: 100000.0 to book essay zoom\nBelieve me, it's going to be your best investment for yourself 😉\n\nCard number: 5614 6822 1973 4029\n\nAfter payment, you should send proof. It can be cheque image/file	1157	2026-02-05 21:22:53.147388+00
33	1	Essay 📝	1159	2026-02-05 21:23:25.621027+00
34	1	None	1161	2026-02-05 21:23:27.288463+00
35	1	Essay 📝	1163	2026-02-05 21:23:28.327326+00
36	1	None	1165	2026-02-05 21:23:29.446774+00
37	1	Essay 📝	1167	2026-02-05 21:23:30.460741+00
38	1	book_essay	1169	2026-02-05 21:23:31.634228+00
39	1	2026-02-10	1170	2026-02-05 21:23:33.006519+00
40	1	2026-02-10 15:00	1170	2026-02-05 21:23:34.190727+00
41	1	cancel_essay	1170	2026-02-05 21:23:35.315017+00
42	1	Great, now you should pay: 100000.0 to book essay zoom\nBelieve me, it's going to be your best investment for yourself 😉\n\nCard number: 5614 6822 1973 4029\n\nAfter payment, you should send proof. It can be cheque image/file	1170	2026-02-05 21:23:35.534242+00
43	1	Essay 📝	1172	2026-02-05 21:23:36.745071+00
44	1	book_essay	1174	2026-02-05 21:23:38.246316+00
45	1	2026-02-12	1175	2026-02-05 21:23:39.665927+00
46	1	2026-02-12 08:00	1175	2026-02-05 21:23:41.00188+00
47	1	cancel_essay	1175	2026-02-05 21:23:43.264429+00
48	1	Great, now you should pay: 100000.0 to book essay zoom\nBelieve me, it's going to be your best investment for yourself 😉\n\nCard number: 5614 6822 1973 4029\n\nAfter payment, you should send proof. It can be cheque image/file	1175	2026-02-05 21:23:43.436514+00
49	1	Championship 🏆	1177	2026-02-05 21:23:44.591936+00
50	1	Essay 📝	1179	2026-02-05 21:23:45.991543+00
51	1	book_essay	1181	2026-02-05 21:23:47.37199+00
52	1	2026-02-12	1182	2026-02-05 21:23:48.5036+00
53	1	2026-02-12 12:00	1182	2026-02-05 21:23:49.416009+00
54	1	cancel_essay	1182	2026-02-05 21:23:50.286263+00
55	1	Great, now you should pay: 100000.0 to book essay zoom\nBelieve me, it's going to be your best investment for yourself 😉\n\nCard number: 5614 6822 1973 4029\n\nAfter payment, you should send proof. It can be cheque image/file	1182	2026-02-05 21:23:50.384734+00
56	1	Championship 🏆	1184	2026-02-05 21:23:51.254898+00
57	1	Championship 🏆	1186	2026-02-05 21:23:52.390966+00
58	1	Championship 🏆	1188	2026-02-05 21:23:53.009661+00
59	1	Championship 🏆	1190	2026-02-05 21:23:53.639827+00
60	1	Championship 🏆	1192	2026-02-05 21:23:54.24785+00
61	1	Championship 🏆	1194	2026-02-05 21:23:54.895449+00
62	1	Championship 🏆	1196	2026-02-05 21:23:55.710646+00
63	1	Championship 🏆	1198	2026-02-05 21:23:56.976318+00
64	1	Essay 📝	1200	2026-02-05 21:23:58.871102+00
65	1	book_essay	1202	2026-02-05 21:24:03.285739+00
66	1	2026-02-10	1203	2026-02-05 21:24:05.629445+00
67	1	2026-02-10 15:00	1203	2026-02-05 21:24:06.678372+00
68	1	None	1204	2026-02-05 21:24:18.826691+00
69	1	Services 📣	1208	2026-02-05 21:24:52.549005+00
70	1	Essay 📝	1210	2026-02-05 21:24:55.466925+00
71	1	book_essay	1212	2026-02-05 21:24:56.826632+00
72	1	Services 📣	1215	2026-02-05 21:53:25.044639+00
73	1	Championship 🏆	1217	2026-02-06 00:11:37.91524+00
74	1	Essay 📝	1219	2026-02-06 12:48:48.295476+00
75	1	None	1221	2026-02-06 12:48:52.95821+00
76	1	Championship 🏆	1223	2026-02-06 13:35:09.322652+00
77	1	Services 📣	1235	2026-02-06 12:06:32.119907+00
78	1	Championship 🏆	1237	2026-02-06 12:06:33.65042+00
79	1	Services 📣	1241	2026-02-06 12:06:35.461765+00
80	1	Essay 📝	1243	2026-02-06 12:06:36.667802+00
81	1	None	1245	2026-02-06 12:06:38.256484+00
82	1	Services 📣	1249	2026-02-06 12:19:25.371718+00
83	1	Championship 🏆	1251	2026-02-06 14:20:11.769784+00
84	1	Essay 📝	1253	2026-02-06 14:20:13.450303+00
85	1	None	1255	2026-02-06 14:20:15.001217+00
86	1	Championship 🏆	1257	2026-02-06 14:20:16.495667+00
87	1	Essay 📝	1259	2026-02-06 14:20:17.818424+00
88	1	None	1261	2026-02-06 14:20:20.267253+00
89	1	Championship 🏆	1263	2026-02-06 14:26:30.363048+00
90	1	Essay 📝	1265	2026-02-06 14:26:31.814486+00
91	1	None	1267	2026-02-06 18:39:10.098368+00
92	1	Championship 🏆	1269	2026-02-06 18:39:13.445239+00
93	1	Services 📣	1273	2026-02-06 18:39:15.563108+00
94	1	Championship 🏆	1276	2026-02-06 19:27:42.709259+00
95	1	Championship 🏆	1278	2026-02-07 07:35:50.198241+00
96	1	Championship 🏆	1280	2026-02-07 08:57:16.959832+00
97	1	Essay 📝	1282	2026-02-07 08:57:18.156527+00
98	1	book_essay	1284	2026-02-07 08:57:22.542293+00
99	1	None	1284	2026-02-07 08:57:25.79928+00
100	1	Championship 🏆	1286	2026-02-07 10:53:36.665054+00
101	1	Championship 🏆	1288	2026-02-07 11:29:06.933285+00
102	1	Essay 📝	1290	2026-02-07 11:29:07.994719+00
103	1	None	1292	2026-02-07 11:29:09.321814+00
104	1	Championship 🏆	1294	2026-02-07 16:49:32.197169+00
105	1	Championship 🏆	1296	2026-02-07 17:53:02.994006+00
106	1	Essay 📝	1298	2026-02-07 17:53:05.106031+00
107	1	None	1300	2026-02-07 17:53:09.873333+00
108	1	Services 📣	1307	2026-02-09 07:28:26.355158+00
109	1	Services 📣	1311	2026-02-09 07:28:32.049386+00
110	1	Essay 📝	1313	2026-02-09 07:28:33.203559+00
111	1	None	1315	2026-02-09 07:28:34.679401+00
112	1	Championship 🏆	1317	2026-02-09 07:28:35.952729+00
113	1	Services 📣	1321	2026-02-09 08:34:50.871343+00
114	1	Championship 🏆	1323	2026-02-09 08:36:30.301409+00
115	1	Championship 🏆	1325	2026-02-09 08:36:31.688438+00
116	1	Championship 🏆	1327	2026-02-09 08:36:32.31906+00
117	1	Championship 🏆	1329	2026-02-09 08:36:32.893252+00
118	1	Championship 🏆	1331	2026-02-09 08:36:33.402292+00
119	1	Championship 🏆	1333	2026-02-09 08:36:34.068683+00
120	1	Championship 🏆	1335	2026-02-09 08:36:34.549583+00
121	1	Championship 🏆	1337	2026-02-09 08:36:35.087084+00
122	1	Championship 🏆	1339	2026-02-09 08:36:35.554506+00
123	1	Championship 🏆	1341	2026-02-09 08:36:37.467497+00
124	1	Championship 🏆	1343	2026-02-09 08:36:37.621912+00
125	1	Championship 🏆	1345	2026-02-09 08:36:37.78155+00
126	1	Championship 🏆	1347	2026-02-09 08:36:37.967874+00
127	1	Championship 🏆	1349	2026-02-09 08:36:38.146142+00
128	1	Championship 🏆	1351	2026-02-09 08:36:38.261271+00
129	1	Championship 🏆	1353	2026-02-09 08:36:38.40832+00
130	1	Championship 🏆	1355	2026-02-09 08:36:38.700775+00
131	1	Championship 🏆	1357	2026-02-09 08:36:38.914486+00
132	1	Championship 🏆	1359	2026-02-09 08:36:39.065941+00
133	1	Championship 🏆	1361	2026-02-09 08:36:39.24983+00
134	1	Championship 🏆	1363	2026-02-09 08:36:39.392798+00
135	1	Championship 🏆	1365	2026-02-09 08:36:39.593057+00
136	1	Championship 🏆	1367	2026-02-09 08:36:39.735775+00
137	1	Championship 🏆	1369	2026-02-09 08:36:39.940813+00
138	1	Championship 🏆	1371	2026-02-09 08:36:40.094993+00
139	1	Championship 🏆	1373	2026-02-09 08:36:40.290707+00
140	1	Championship 🏆	1375	2026-02-09 08:36:40.481401+00
141	1	Championship 🏆	1377	2026-02-09 08:36:40.640433+00
142	1	Championship 🏆	1378	2026-02-09 08:36:40.811953+00
143	1	Championship 🏆	1381	2026-02-09 08:36:41.011534+00
144	1	Championship 🏆	1383	2026-02-09 08:36:41.185067+00
145	1	Championship 🏆	1385	2026-02-09 08:36:41.288511+00
146	1	Championship 🏆	1387	2026-02-09 08:36:41.570466+00
147	1	Championship 🏆	1389	2026-02-09 08:36:41.676869+00
148	1	Championship 🏆	1391	2026-02-09 08:36:41.837825+00
149	1	Championship 🏆	1393	2026-02-09 08:36:42.062318+00
150	1	Championship 🏆	1395	2026-02-09 08:36:42.324686+00
151	1	Championship 🏆	1397	2026-02-09 08:36:42.504035+00
152	1	Championship 🏆	1398	2026-02-09 08:36:42.562282+00
153	1	Championship 🏆	1401	2026-02-09 08:36:42.820627+00
154	1	Championship 🏆	1403	2026-02-09 08:36:43.078865+00
155	1	Championship 🏆	1405	2026-02-09 08:36:43.274814+00
156	1	Championship 🏆	1407	2026-02-09 08:36:43.353777+00
157	1	Championship 🏆	1409	2026-02-09 08:36:43.548379+00
158	1	Championship 🏆	1411	2026-02-09 08:36:43.908852+00
159	1	Championship 🏆	1412	2026-02-09 08:36:43.939756+00
160	1	Championship 🏆	1415	2026-02-09 08:36:44.107358+00
161	1	Championship 🏆	1416	2026-02-09 08:36:44.241678+00
162	1	Championship 🏆	1419	2026-02-09 08:36:44.511995+00
163	1	Championship 🏆	1421	2026-02-09 08:36:44.672669+00
164	1	Championship 🏆	1423	2026-02-09 08:36:44.873781+00
165	1	Championship 🏆	1425	2026-02-09 08:36:45.042451+00
166	1	Championship 🏆	1427	2026-02-09 08:36:45.297112+00
167	1	Championship 🏆	1429	2026-02-09 08:36:45.496779+00
168	1	Championship 🏆	1431	2026-02-09 08:36:45.820844+00
169	1	Championship 🏆	1432	2026-02-09 08:36:45.84998+00
170	1	Championship 🏆	1435	2026-02-09 08:36:46.066663+00
171	1	Championship 🏆	1437	2026-02-09 08:36:46.204746+00
172	1	Championship 🏆	1439	2026-02-09 08:36:46.368276+00
173	1	Championship 🏆	1441	2026-02-09 08:36:46.589179+00
174	1	Championship 🏆	1443	2026-02-09 08:36:46.829915+00
175	1	Championship 🏆	1445	2026-02-09 08:36:47.140313+00
176	1	Championship 🏆	1447	2026-02-09 08:36:47.342379+00
177	1	Championship 🏆	1448	2026-02-09 08:36:47.511523+00
178	1	Championship 🏆	1450	2026-02-09 08:36:47.55771+00
179	1	Championship 🏆	1453	2026-02-09 08:36:47.958407+00
180	1	Championship 🏆	1454	2026-02-09 08:36:47.996568+00
181	1	Championship 🏆	1457	2026-02-09 08:36:48.153837+00
182	1	Championship 🏆	1459	2026-02-09 08:36:48.357357+00
183	1	Championship 🏆	1461	2026-02-09 08:36:48.584684+00
184	1	Championship 🏆	1463	2026-02-09 08:36:48.779309+00
185	1	Championship 🏆	1465	2026-02-09 08:36:49.013244+00
186	1	Championship 🏆	1467	2026-02-09 08:36:49.184349+00
187	1	Championship 🏆	1469	2026-02-09 08:36:49.387359+00
188	1	Championship 🏆	1471	2026-02-09 08:36:49.585768+00
189	1	Championship 🏆	1473	2026-02-09 08:36:49.801986+00
190	1	Championship 🏆	1475	2026-02-09 08:36:53.166582+00
191	1	Championship 🏆	1477	2026-02-09 08:36:53.997306+00
192	1	Championship 🏆	1478	2026-02-09 08:36:54.039385+00
193	1	Championship 🏆	1481	2026-02-09 08:36:54.095051+00
194	1	Championship 🏆	1479	2026-02-09 08:36:54.167981+00
195	1	Championship 🏆	1484	2026-02-09 08:36:54.272577+00
196	1	Championship 🏆	1482	2026-02-09 08:36:54.274382+00
197	1	Services 📣	1492	2026-02-09 08:38:09.712261+00
198	1	Services 📣	1494	2026-02-09 08:38:09.854759+00
199	1	Essay 📝	1496	2026-02-09 08:38:10.039308+00
200	1	Essay 📝	1497	2026-02-09 08:38:10.097463+00
201	1	Essay 📝	1501	2026-02-09 08:38:10.307161+00
202	1	Services 📣	1508	2026-02-09 08:40:08.358992+00
203	1	Services 📣	1509	2026-02-09 08:40:08.382089+00
204	1	Services 📣	1510	2026-02-09 08:40:08.410608+00
205	1	Services 📣	1514	2026-02-09 08:40:08.557992+00
206	1	Services 📣	1516	2026-02-09 08:40:08.671877+00
207	1	Essay 📝	1518	2026-02-09 08:40:08.783789+00
208	1	Essay 📝	1521	2026-02-09 08:40:09.077597+00
209	1	None	1523	2026-02-09 08:40:23.600771+00
210	1	Championship 🏆	1525	2026-02-09 08:40:30.491141+00
211	1	Championship 🏆	1527	2026-02-09 08:40:30.800828+00
212	1	Championship 🏆	1528	2026-02-09 08:40:30.839924+00
213	1	Championship 🏆	1531	2026-02-09 08:40:31.109252+00
214	1	Championship 🏆	1532	2026-02-09 08:40:31.127582+00
215	1	Championship 🏆	1535	2026-02-09 08:40:31.303932+00
216	1	Championship 🏆	1536	2026-02-09 08:40:31.330403+00
217	1	Championship 🏆	1539	2026-02-09 08:40:31.484628+00
218	1	Championship 🏆	1540	2026-02-09 08:40:31.51345+00
219	1	Championship 🏆	1543	2026-02-09 08:40:31.72312+00
220	1	Championship 🏆	1545	2026-02-09 08:40:31.796992+00
221	1	Championship 🏆	1547	2026-02-09 08:40:31.888828+00
222	1	Championship 🏆	1549	2026-02-09 08:40:32.010769+00
223	1	Championship 🏆	1551	2026-02-09 08:40:32.199039+00
224	1	Championship 🏆	1553	2026-02-09 08:40:32.325746+00
225	1	Championship 🏆	1554	2026-02-09 08:40:32.413381+00
226	1	Championship 🏆	1557	2026-02-09 08:40:33.483026+00
227	1	Championship 🏆	1558	2026-02-09 08:40:33.489291+00
228	1	Championship 🏆	1559	2026-02-09 08:40:33.491277+00
229	1	Championship 🏆	1562	2026-02-09 08:40:33.755704+00
230	1	Championship 🏆	1561	2026-02-09 08:40:33.756351+00
231	1	Championship 🏆	1560	2026-02-09 08:40:33.759039+00
232	1	Championship 🏆	1565	2026-02-09 08:40:33.9437+00
233	1	Championship 🏆	1563	2026-02-09 08:40:33.964912+00
234	1	Championship 🏆	1566	2026-02-09 08:40:33.968252+00
235	1	Championship 🏆	1564	2026-02-09 08:40:33.981292+00
236	1	Championship 🏆	1567	2026-02-09 08:40:33.981486+00
237	1	Championship 🏆	1570	2026-02-09 08:40:34.104673+00
238	1	Championship 🏆	1576	2026-02-09 08:40:34.199801+00
239	1	Championship 🏆	1578	2026-02-09 08:40:34.254294+00
240	1	Championship 🏆	1579	2026-02-09 08:40:34.257824+00
241	1	Championship 🏆	1586	2026-02-09 08:40:34.434133+00
242	1	Championship 🏆	1589	2026-02-09 08:40:34.562967+00
243	1	Championship 🏆	1591	2026-02-09 08:40:34.659705+00
244	1	Championship 🏆	1593	2026-02-09 08:40:34.783474+00
245	1	Championship 🏆	1594	2026-02-09 08:40:34.861691+00
246	1	Championship 🏆	1597	2026-02-09 08:40:35.077412+00
247	1	Championship 🏆	1599	2026-02-09 08:40:35.168943+00
248	1	Championship 🏆	1600	2026-02-09 08:40:35.297431+00
249	1	Championship 🏆	1603	2026-02-09 08:40:35.503788+00
250	1	Championship 🏆	1604	2026-02-09 08:40:35.503653+00
251	1	Championship 🏆	1607	2026-02-09 08:40:35.704624+00
252	1	Championship 🏆	1609	2026-02-09 08:40:35.912587+00
253	1	Championship 🏆	1610	2026-02-09 08:40:35.937817+00
254	1	Championship 🏆	1612	2026-02-09 08:40:36.105808+00
255	1	Championship 🏆	1615	2026-02-09 08:40:36.402941+00
256	1	Championship 🏆	1616	2026-02-09 08:40:36.423265+00
257	1	Championship 🏆	1617	2026-02-09 08:40:36.468808+00
258	1	Championship 🏆	1621	2026-02-09 08:40:36.683529+00
259	1	Championship 🏆	1622	2026-02-09 08:40:36.719133+00
260	1	Championship 🏆	1625	2026-02-09 08:40:42.326807+00
261	1	Championship 🏆	1627	2026-02-09 08:40:42.552255+00
262	1	Championship 🏆	1628	2026-02-09 08:40:42.580102+00
263	1	Championship 🏆	1629	2026-02-09 08:40:42.602476+00
264	1	Championship 🏆	1631	2026-02-09 08:40:42.622212+00
265	1	Championship 🏆	1633	2026-02-09 08:40:42.656102+00
266	1	Championship 🏆	1635	2026-02-09 08:40:42.680301+00
267	1	Championship 🏆	1637	2026-02-09 08:40:42.717415+00
268	1	Championship 🏆	1639	2026-02-09 08:40:42.733381+00
269	1	Championship 🏆	1641	2026-02-09 08:40:42.762319+00
270	1	Championship 🏆	1643	2026-02-09 08:40:42.786081+00
271	1	Championship 🏆	1644	2026-02-09 08:40:42.816963+00
272	1	Championship 🏆	1646	2026-02-09 08:40:42.838207+00
273	1	Championship 🏆	1649	2026-02-09 08:40:42.858103+00
274	1	Championship 🏆	1651	2026-02-09 08:40:42.905315+00
275	1	Championship 🏆	1653	2026-02-09 08:40:42.920791+00
276	1	Championship 🏆	1655	2026-02-09 08:40:42.938405+00
277	1	Championship 🏆	1657	2026-02-09 08:40:42.969002+00
278	1	Championship 🏆	1659	2026-02-09 08:40:43.008396+00
279	1	Championship 🏆	1661	2026-02-09 08:40:43.041183+00
280	1	Championship 🏆	1663	2026-02-09 08:40:43.07373+00
281	1	Championship 🏆	1665	2026-02-09 08:40:43.094975+00
282	1	Championship 🏆	1667	2026-02-09 08:40:43.114826+00
283	1	Championship 🏆	1671	2026-02-09 08:43:46.196346+00
284	1	Championship 🏆	1673	2026-02-09 09:32:41.403882+00
285	1	Services 📣	1715	2026-02-09 10:42:47.374526+00
286	1	Essay 📝	1717	2026-02-09 10:42:48.316597+00
287	1	None	1719	2026-02-09 10:42:49.587559+00
288	1	Championship 🏆	1723	2026-02-09 10:42:51.31334+00
289	1	Championship 🏆	1725	2026-02-09 10:42:54.412373+00
290	1	Championship 🏆	1727	2026-02-09 10:42:54.729052+00
291	1	Championship 🏆	1729	2026-02-09 10:42:54.976182+00
292	1	Championship 🏆	1743	2026-02-09 10:42:56.626489+00
293	1	Championship 🏆	1781	2026-02-09 10:42:59.62831+00
294	1	Championship 🏆	1783	2026-02-09 10:42:59.758007+00
295	1	Championship 🏆	1785	2026-02-09 10:43:00.009305+00
296	1	Championship 🏆	1801	2026-02-09 10:43:02.476592+00
297	1	Championship 🏆	1827	2026-02-09 10:43:04.797315+00
298	1	Championship 🏆	1829	2026-02-09 10:43:04.871829+00
299	1	Championship 🏆	1833	2026-02-09 10:43:05.177472+00
300	1	Championship 🏆	1839	2026-02-09 10:43:08.971991+00
301	1	Championship 🏆	1869	2026-02-09 10:43:40.652289+00
302	1	Championship 🏆	1871	2026-02-09 10:43:40.910444+00
303	1	Championship 🏆	1873	2026-02-09 10:43:41.128842+00
304	1	Championship 🏆	1875	2026-02-09 10:43:41.365991+00
305	1	Championship 🏆	1919	2026-02-09 10:43:45.916065+00
306	1	Championship 🏆	1921	2026-02-09 10:43:46.170922+00
307	1	Championship 🏆	1922	2026-02-09 10:43:46.204861+00
308	1	Championship 🏆	1925	2026-02-09 10:43:46.470282+00
309	1	Services 📣	2016	2026-02-09 10:45:34.193181+00
310	1	Services 📣	2018	2026-02-09 10:45:45.865598+00
311	1	Services 📣	2020	2026-02-09 10:45:46.706342+00
312	1	Services 📣	2022	2026-02-09 10:45:47.697314+00
313	1	Services 📣	2024	2026-02-09 10:45:48.551028+00
314	1	Services 📣	2030	2026-02-09 10:45:51.448443+00
315	1	Services 📣	2032	2026-02-09 10:45:51.901804+00
316	1	Services 📣	2036	2026-02-09 10:45:52.897757+00
317	1	Services 📣	2038	2026-02-09 10:45:53.566789+00
318	1	Services 📣	2052	2026-02-09 10:45:56.51704+00
319	1	Services 📣	2056	2026-02-09 10:45:57.334554+00
320	1	Services 📣	2060	2026-02-09 10:46:03.061938+00
321	1	Essay 📝	2062	2026-02-09 10:46:05.438655+00
322	1	book_essay	2064	2026-02-09 10:46:06.717965+00
323	1	book_essay	2064	2026-02-09 10:46:08.718341+00
324	1	book_essay	2064	2026-02-09 10:46:09.818764+00
325	1	book_essay	2064	2026-02-09 10:46:13.742059+00
326	1	book_essay	2064	2026-02-09 10:46:14.462569+00
327	1	book_essay	2064	2026-02-09 10:46:15.247166+00
328	1	book_essay	2064	2026-02-09 10:46:17.625534+00
329	1	book_essay	2064	2026-02-09 10:46:19.200509+00
330	1	book_essay	2064	2026-02-09 10:46:21.052083+00
331	1	book_essay	2064	2026-02-09 10:46:23.585316+00
332	1	book_essay	2064	2026-02-09 10:46:24.560676+00
333	1	book_essay	2064	2026-02-09 10:46:25.466637+00
334	1	book_essay	2064	2026-02-09 10:46:26.245422+00
335	1	book_essay	2064	2026-02-09 10:46:31.361599+00
336	1	book_essay	2064	2026-02-09 10:46:31.70537+00
337	1	book_essay	2064	2026-02-09 10:46:32.808071+00
338	1	book_essay	2064	2026-02-09 10:46:33.241067+00
339	1	book_essay	2064	2026-02-09 10:46:36.921606+00
340	1	book_essay	2064	2026-02-09 10:49:49.892706+00
341	1	book_essay	2064	2026-02-09 10:49:50.578388+00
342	1	book_essay	2064	2026-02-09 10:49:50.928474+00
343	1	book_essay	2064	2026-02-09 10:49:51.816246+00
344	1	book_essay	2064	2026-02-09 10:49:56.242324+00
345	1	book_essay	2064	2026-02-09 10:49:56.63214+00
346	1	book_essay	2064	2026-02-09 10:49:57.296399+00
347	1	book_essay	2064	2026-02-09 10:49:57.663959+00
348	1	book_essay	2064	2026-02-09 10:50:02.66321+00
349	1	book_essay	2064	2026-02-09 10:50:03.133568+00
350	1	book_essay	2064	2026-02-09 10:50:03.937416+00
351	1	book_essay	2064	2026-02-09 10:50:04.402849+00
352	1	None	2064	2026-02-09 10:50:13.690803+00
353	1	Championship 🏆	2066	2026-02-09 10:50:17.631902+00
354	1	Championship 🏆	2068	2026-02-09 10:50:17.876782+00
355	1	Championship 🏆	2070	2026-02-09 10:50:18.05848+00
356	1	Championship 🏆	2075	2026-02-09 10:50:18.632314+00
357	1	Championship 🏆	2088	2026-02-09 11:02:34.420456+00
358	1	Championship 🏆	2090	2026-02-09 11:02:35.310719+00
359	1	Championship 🏆	2092	2026-02-09 11:02:36.094971+00
360	1	Championship 🏆	2094	2026-02-09 11:02:36.925483+00
361	1	Championship 🏆	2098	2026-02-09 11:02:39.774741+00
362	1	Championship 🏆	2100	2026-02-09 11:02:40.693059+00
363	1	Championship 🏆	2102	2026-02-09 11:02:41.424372+00
364	1	Championship 🏆	2104	2026-02-09 11:02:42.126899+00
365	1	Championship 🏆	2112	2026-02-09 11:02:44.955935+00
366	1	Championship 🏆	2122	2026-02-09 11:02:45.854123+00
367	1	Championship 🏆	2128	2026-02-09 11:02:46.792297+00
368	1	Championship 🏆	2134	2026-02-09 11:18:33.047764+00
369	1	Championship 🏆	2136	2026-02-09 11:18:38.771305+00
370	1	Championship 🏆	2138	2026-02-09 11:18:39.960111+00
371	1	Championship 🏆	2140	2026-02-09 11:18:44.002058+00
372	1	Championship 🏆	2142	2026-02-09 11:18:44.520555+00
373	1	Championship 🏆	2144	2026-02-09 11:18:44.725664+00
374	1	Championship 🏆	2146	2026-02-09 11:18:45.107541+00
375	1	Championship 🏆	2154	2026-02-09 11:20:03.211321+00
376	1	Championship 🏆	2156	2026-02-09 11:20:03.764709+00
377	1	Championship 🏆	2158	2026-02-09 11:20:03.8918+00
378	1	Championship 🏆	2160	2026-02-09 11:20:04.232976+00
379	1	Services 📣	2174	2026-02-09 19:09:32.715995+00
380	1	Services 📣	2178	2026-02-09 19:09:39.207585+00
381	1	Services 📣	2182	2026-02-09 19:09:41.839153+00
382	1	Services 📣	2308	2026-02-10 11:32:54.160768+00
383	1	Services 📣	2312	2026-02-10 12:21:35.511171+00
384	1	Services 📣	2316	2026-02-10 12:21:42.325681+00
385	1	Championship 🏆	2318	2026-02-10 12:21:43.634857+00
386	1	Services 📣	2324	2026-02-10 12:21:47.71649+00
387	1	Essay 📝	2326	2026-02-10 12:21:48.83634+00
388	1	None	2328	2026-02-10 12:21:53.331629+00
389	1	Essay 📝	2330	2026-02-10 12:21:56.6528+00
390	1	None	2332	2026-02-10 12:21:58.893416+00
391	1	Essay 📝	2334	2026-02-10 12:22:02.133622+00
392	1	book_essay	2336	2026-02-10 12:22:03.595993+00
393	1	None	2336	2026-02-10 12:22:05.292982+00
394	1	Services 📣	2340	2026-02-11 02:17:51.295537+00
395	1	Services 📣	2346	2026-02-11 18:28:32.441586+00
396	1	Services 📣	2352	2026-02-12 13:49:29.913597+00
397	1	Services 📣	2356	2026-02-14 15:43:11.778622+00
398	1	Services 📣	2360	2026-02-14 15:43:15.24088+00
399	1	Essay 📝	2362	2026-02-14 15:43:16.499473+00
400	1	book_essay	2364	2026-02-14 15:43:18.398122+00
401	1	None	2364	2026-02-14 15:43:20.231964+00
402	1	Services 📣	2368	2026-02-14 17:44:46.432137+00
403	1	Services 📣	2373	2026-02-14 17:44:55.56175+00
404	1	Championship 🏆	2375	2026-02-14 17:46:50.277576+00
405	1	Essay 📝	2377	2026-02-14 17:46:53.418042+00
\.


--
-- Data for Name: tg_group_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tg_group_model (idn, group_id, status, created_at) FROM stdin;
1	-1003847126126	1	2026-02-05 00:24:47.588796+00
\.


--
-- Data for Name: tg_group_section_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.tg_group_section_model (idn, group_idn, section_id, type_connected, status, created_at) FROM stdin;
1	1	227	0	1	2026-02-05 00:24:47.824672+00
2	1	228	1	1	2026-02-05 00:24:47.954743+00
3	1	229	2	1	2026-02-05 00:24:48.05516+00
4	1	230	3	1	2026-02-05 00:24:48.176841+00
5	1	231	4	1	2026-02-05 00:24:48.31151+00
\.


--
-- Data for Name: transaction_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.transaction_model (idn, balance_idn, created_by, amount, proof, for_what, for_what_idn, is_benefit, created_at) FROM stdin;
\.


--
-- Data for Name: user_model; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.user_model (idn, chat_id, id_name, phone_number, tg_username, tg_first_name, tg_last_name, name, age, used, role, lang, active, log_in, deleted, created_at, updated_at, deleted_at) FROM stdin;
1	2139292627	mf7662	+998911853616	egamberdiyev_abdurahim	MasterPhone	\N	Abdurahim Egamberdiyev	18	485	1	en	1	1	0	2026-02-05 00:37:05.453865+00	\N	\N
\.


--
-- Name: balance_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.balance_model_idn_seq', 1, true);


--
-- Name: errors_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.errors_model_idn_seq', 1, false);


--
-- Name: essay_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.essay_model_idn_seq', 1, true);


--
-- Name: essay_user_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.essay_user_model_idn_seq', 1, true);


--
-- Name: essentials_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.essentials_model_idn_seq', 1, true);


--
-- Name: event_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.event_model_idn_seq', 1, false);


--
-- Name: event_user_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.event_user_model_idn_seq', 1, false);


--
-- Name: history_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.history_model_idn_seq', 405, true);


--
-- Name: tg_group_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tg_group_model_idn_seq', 1, true);


--
-- Name: tg_group_section_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.tg_group_section_model_idn_seq', 5, true);


--
-- Name: transaction_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.transaction_model_idn_seq', 1, false);


--
-- Name: user_model_idn_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.user_model_idn_seq', 1, true);


--
-- Name: balance_model balance_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.balance_model
    ADD CONSTRAINT balance_model_pkey PRIMARY KEY (idn);


--
-- Name: errors_model errors_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.errors_model
    ADD CONSTRAINT errors_model_pkey PRIMARY KEY (idn);


--
-- Name: essay_model essay_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.essay_model
    ADD CONSTRAINT essay_model_pkey PRIMARY KEY (idn);


--
-- Name: essay_user_model essay_user_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.essay_user_model
    ADD CONSTRAINT essay_user_model_pkey PRIMARY KEY (idn);


--
-- Name: essentials_model essentials_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.essentials_model
    ADD CONSTRAINT essentials_model_pkey PRIMARY KEY (idn);


--
-- Name: event_model event_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_model
    ADD CONSTRAINT event_model_pkey PRIMARY KEY (idn);


--
-- Name: event_user_model event_user_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.event_user_model
    ADD CONSTRAINT event_user_model_pkey PRIMARY KEY (idn);


--
-- Name: history_model history_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.history_model
    ADD CONSTRAINT history_model_pkey PRIMARY KEY (idn);


--
-- Name: tg_group_model tg_group_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tg_group_model
    ADD CONSTRAINT tg_group_model_pkey PRIMARY KEY (idn);


--
-- Name: tg_group_section_model tg_group_section_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.tg_group_section_model
    ADD CONSTRAINT tg_group_section_model_pkey PRIMARY KEY (idn);


--
-- Name: transaction_model transaction_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.transaction_model
    ADD CONSTRAINT transaction_model_pkey PRIMARY KEY (idn);


--
-- Name: user_model user_model_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.user_model
    ADD CONSTRAINT user_model_pkey PRIMARY KEY (idn);


--
-- PostgreSQL database dump complete
--

\unrestrict TV1GW9zAc9Xb8ewMW3ZvsZfZz4BB7az7OI8n9m44djdsUzt3GINb96lz00OUmEt

